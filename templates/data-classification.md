# {{company_name}} Data Classification & Handling Policy

> **Control mapping.** ISO/IEC 27001:2022 Annex A 5.12 (classification of information), 5.13 (labelling of information), 5.14 (information transfer), 8.10 (information deletion), 8.11 (data masking), 8.12 (data leakage prevention) · SOC 2 CC6.1, CC6.5, and the Confidentiality (C1.1–C1.2) and Privacy criteria.

**Owner:** {{policy_owner}} · **Approver:** {{approver}} · **Classification:** Internal · **Applies to:** all {{company_name}} personnel, contractors, and systems that handle company data.

## 1. Purpose
This policy defines how {{company_name}} classifies information by sensitivity and how each class must be handled, so that {{data_types}} receive protection proportionate to their risk, in line with {{frameworks}}.

## 2. Scope
This policy applies to all information {{company_name}} owns or processes, in any format, across {{cloud_providers}} and on-premises systems, throughout its lifecycle from creation to disposal.

## 3. Classification Levels
- **Restricted** — highest sensitivity; unauthorised disclosure would cause serious harm. Typically includes regulated data such as {{data_types}}.
- **Confidential** — internal information whose disclosure would cause moderate harm (contracts, financials, source code).
- **Internal** — day-to-day information intended for staff but not the public.
- **Public** — information approved for public release.

## 4. Labelling
Information and the systems that store it are labelled with their classification where practical. In the absence of a label, information is treated as **Confidential** by default.

## 5. Handling Requirements
- **Access:** Restricted and Confidential data follow least-privilege access (see the Access Control Policy).
- **Storage:** Restricted data is encrypted at rest and kept only in approved {{cloud_providers}} services; it is not copied to personal devices or unapproved services.
- **Transfer:** Restricted and Confidential data are encrypted in transit and shared only through approved channels with authorised recipients.
- **Masking:** Production {{data_types}} are masked or synthetic in test and development environments.

## 6. Retention and Disposal
Data is retained only as long as needed for business, legal, or regulatory purposes, then securely deleted or destroyed so it cannot be reconstructed. Retention periods for {{data_types}} follow applicable regulation and the data retention schedule.

## 7. Leakage Prevention
{{company_name}} applies controls to detect and prevent unauthorised movement of Restricted data, and users report any suspected loss or exposure of {{data_types}} to {{security_contact}} without delay.

## 8. Roles and Responsibilities
- **Data owners** assign classifications and approve handling exceptions.
- **{{policy_owner}}** maintains this policy and the classification scheme.
- **All personnel** classify and handle information according to this policy.

## 9. Review
This policy is reviewed at least annually by {{policy_owner}} and approved by {{approver}}.
