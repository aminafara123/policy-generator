"""Offline tests. No network, no API key. The LLM is mocked or skipped entirely."""
import pytest

import generate

SAMPLE = {
    "company": {
        "name": "Acme Robotics",
        "industry": "industrial IoT",
        "size": "120 employees",
        "cloud_providers": ["AWS", "Azure"],
        "data_types": ["Customer PII", "Telemetry"],
        "frameworks": ["ISO/IEC 27001:2022", "SOC 2"],
        "security_contact": "sec@acme.example",
        "policy_owner": "CISO",
        "approver": "CEO",
    },
    "version": "0.1 (Draft)",
}


# --- template loading -------------------------------------------------------
def test_all_templates_load_with_placeholders_and_mapping():
    for key in generate.POLICIES:
        text = generate.load_template(key)
        assert text.strip(), f"{key} template is empty"
        assert "{{" in text, f"{key} has no placeholders"
        assert "ISO/IEC 27001" in text and "SOC 2" in text, f"{key} missing control mapping"
        # the header/body split must find at least one section heading
        header, body = generate._split_header_body(text)
        assert body.lstrip().startswith("## "), f"{key} has no '## ' sections"


# --- placeholder substitution ----------------------------------------------
def test_substitution_fills_known_and_flags_missing():
    values = generate.flatten_profile(SAMPLE)
    assert values["company_name"] == "Acme Robotics"
    assert values["cloud_providers"] == "AWS, Azure"  # list joined

    text = "Company {{company_name}} uses {{cloud_providers}}."
    out, missing = generate.substitute(text, values)
    assert out == "Company Acme Robotics uses AWS, Azure."
    assert missing == []

    out2, missing2 = generate.substitute("Owner: {{nonexistent}}", values)
    assert "[REVIEW: nonexistent]" in out2
    assert missing2 == ["nonexistent"]


def test_filled_template_has_no_leftover_placeholders():
    values = generate.flatten_profile(SAMPLE)
    filled, missing = generate.substitute(generate.load_template("access-control"), values)
    assert "{{" not in filled
    assert missing == []  # sample profile provides every placeholder the template uses


# --- selection logic --------------------------------------------------------
def test_selection_defaults_to_profile_list_then_all():
    profile = {"policies": ["access-control", "incident-response"]}
    assert generate.select_policies(profile) == ["access-control", "incident-response"]
    # 'all' overrides the profile list
    assert generate.select_policies(profile, "all") == list(generate.POLICIES)
    # empty profile -> all
    assert generate.select_policies({}) == list(generate.POLICIES)


def test_selection_keeps_canonical_order_and_dedupes():
    got = generate.select_policies({}, ["incident-response", "access-control", "access-control"])
    assert got == ["access-control", "incident-response"]


def test_selection_rejects_unknown_key():
    with pytest.raises(ValueError):
        generate.select_policies({}, ["not-a-policy"])


# --- LLM tailoring + deterministic fallback ---------------------------------
def test_tailor_fallback_on_llm_failure():
    def boom(*a, **k):
        raise RuntimeError("endpoint down")

    body = "## 1. Purpose\nText.\n\n## 2. Scope\nMore."
    out, used = generate.tailor(body, SAMPLE, llm=boom)
    assert used is False
    assert out == body  # unchanged, still a complete body


def test_tailor_uses_llm_when_headings_preserved():
    body = "## 1. Purpose\nText.\n\n## 2. Scope\nMore."

    def good(prompt, system=None, **k):
        return "## 1. Purpose\nExpanded, company-specific purpose.\n\n## 2. Scope\nExpanded scope."

    out, used = generate.tailor(body, SAMPLE, llm=good)
    assert used is True
    assert "Expanded" in out


def test_tailor_rejects_llm_that_drops_headings():
    body = "## 1. Purpose\nText.\n\n## 2. Scope\nMore."

    def bad(prompt, system=None, **k):
        return "Here is a totally rewritten doc with no original headings."

    out, used = generate.tailor(body, SAMPLE, llm=bad)
    assert used is False
    assert out == body


def test_no_llm_flag_skips_tailoring():
    body = "## 1. Purpose\nText."
    out, used = generate.tailor(body, SAMPLE, llm=lambda *a, **k: "x", no_llm=True)
    assert used is False and out == body


# --- end-to-end + docx generation ------------------------------------------
def test_build_document_is_labelled_and_complete():
    md, used = generate.build_document("incident-response", SAMPLE, no_llm=True)
    assert "AI-ASSISTED DRAFT" in md
    assert "Document Control" in md
    assert "Acme Robotics" in md
    assert "{{" not in md  # no stray placeholders
    assert used is False


def test_docx_generation_creates_file_with_expected_headings(tmp_path):
    from docx import Document

    results = generate.generate(SAMPLE, ["access-control"], tmp_path, no_llm=True)
    key, md_path, docx_path, used = results[0]

    assert md_path.exists() and docx_path.exists()
    assert docx_path.stat().st_size > 0

    doc = Document(str(docx_path))
    texts = [p.text for p in doc.paragraphs]
    joined = "\n".join(texts)

    # title + numbered section headings present
    assert any("Access Control Policy" in t for t in texts)
    assert any("1. Purpose" in t for t in texts)
    assert any("Document Control" in t for t in texts)
    # AI-assisted draft label present in body
    assert "AI-ASSISTED DRAFT" in joined

    # heading styles actually applied (not just plain paragraphs)
    styles = {p.style.name for p in doc.paragraphs}
    assert any(s.startswith("Heading") or s == "Title" for s in styles)

    # approval table rendered as a real docx table containing "Version"
    all_cells = [c.text for tbl in doc.tables for row in tbl.rows for c in row.cells]
    assert "Version" in all_cells

    # footer carries the review-required notice
    footer_text = doc.sections[0].footer.paragraphs[0].text
    assert "review" in footer_text.lower() and "approval" in footer_text.lower()
