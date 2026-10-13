# {{company_name}} Incident Response Policy

> **Control mapping.** ISO/IEC 27001:2022 Annex A 5.24 (incident management planning), 5.25 (assessment & decision), 5.26 (response), 5.27 (learning from incidents), 5.28 (evidence collection), 6.8 (reporting events) · SOC 2 CC7.3, CC7.4, CC7.5.

**Owner:** {{policy_owner}} · **Approver:** {{approver}} · **Classification:** Internal · **Applies to:** all {{company_name}} personnel, contractors, and systems.

## 1. Purpose
This policy ensures {{company_name}} detects, responds to, and learns from information security incidents quickly and consistently, limiting harm to the business and to the owners of {{data_types}}, in line with {{frameworks}}.

## 2. Scope
This policy covers all suspected and confirmed security incidents affecting {{company_name}} systems, data, or services, including those hosted on {{cloud_providers}}, and all personnel who may detect or respond to them.

## 3. Definitions
A **security event** is an observable occurrence that may be relevant to security. A **security incident** is an event, or series of events, that compromises or threatens the confidentiality, integrity, or availability of information or systems.

## 4. Reporting
All personnel report suspected incidents immediately to {{security_contact}}. Early reporting is encouraged and never penalised; delay or concealment is a policy violation. Reports should include what happened, when, and what systems or data may be affected.

## 5. Severity and Triage
Reported events are triaged and assigned a severity based on impact and urgency. Incidents involving {{data_types}}, customer-facing outages, or confirmed unauthorised access are treated as high severity and escalated to {{policy_owner}} without delay.

## 6. Response Process
1. **Identify** — confirm whether an incident has occurred and record initial facts.
2. **Contain** — limit the spread and impact (isolate systems, revoke access, block indicators).
3. **Eradicate** — remove the cause (malware, compromised credentials, vulnerable configuration).
4. **Recover** — restore affected systems and data from trusted sources and confirm normal operation.
5. **Communicate** — notify stakeholders, and where {{data_types}} are involved, assess legal and regulatory breach-notification obligations with {{approver}}.

## 7. Evidence and Forensics
Where an incident may involve legal action or regulatory reporting, evidence is preserved and handled to maintain its integrity and chain of custody. Actions taken during the incident are logged with timestamps.

## 8. Post-Incident Review
After significant incidents, {{policy_owner}} leads a review to capture root cause, lessons learned, and corrective actions. Actions are tracked to closure and feed back into controls and this policy.

## 9. Roles and Responsibilities
- **{{policy_owner}}** coordinates incident response and owns this policy.
- **{{approver}}** is engaged for high-severity incidents and external communications.
- **All personnel** report promptly and cooperate with response.

## 10. Review
This policy, and the incident response plan it supports, are reviewed at least annually and tested periodically by {{policy_owner}}.
