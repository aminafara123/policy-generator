# 60-second demo script

Goal: show that a short company profile becomes review-ready ISO 27001 / SOC 2 policy drafts in Markdown and Word, with the AI output clearly labelled for human approval.

Record a terminal plus a quick open of the generated .docx. Keep it under a minute.

## Setup (before recording)

```bash
cd policy-generator
make install          # python-docx, PyYAML, pytest
```

If you want the real LLM tailoring on camera, have Ollama running with the model in `.env.example`. If not, the fallback still produces complete drafts, so the demo works offline either way.

## Recording (the 60 seconds)

1) Show the input is just a profile (3-4 seconds):
```bash
sed -n '1,20p' profile.example.yaml
```

2) Show the available policies (3 seconds):
```bash
python generate.py --list
```

3) Run the generator (10 seconds). Point out the `[LLM-tailored]` vs `[deterministic fallback]` tag and the final "review and approve before use" line:
```bash
make run
```

4) Show the outputs (3 seconds):
```bash
ls output/
```

5) Open one Word file and scroll (15-20 seconds). Call out, on screen:
   - the title and the numbered sections
   - the Document Control / approval table
   - the "AI-ASSISTED DRAFT" banner near the top
   - the page footer "requires review and approval ... before use"
```bash
# macOS: open output/access-control.docx
# Linux: xdg-open output/access-control.docx
# Windows: start output/access-control.docx
```

6) Prove the gate (10 seconds):
```bash
make test
```
Say out loud: "Tests pass with no network and no API key. The LLM is mocked, and the deterministic core is what's tested."

## The one-line takeaway

"A company profile in, eight control-mapped policy drafts out, in Markdown and Word, labelled AI-assisted and left for a human to approve."
