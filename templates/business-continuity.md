# {{company_name}} Business Continuity & Disaster Recovery Policy

> **Control mapping.** ISO/IEC 27001:2022 Annex A 5.29 (information security during disruption), 5.30 (ICT readiness for business continuity), 8.13 (information backup), 8.14 (redundancy of processing facilities) · SOC 2 Availability criteria A1.1–A1.3, CC7.5.

**Owner:** {{policy_owner}} · **Approver:** {{approver}} · **Classification:** Internal · **Applies to:** all {{company_name}} personnel, critical systems, and service providers.

## 1. Purpose
This policy ensures {{company_name}} can continue, or quickly resume, its critical operations and protect {{data_types}} during and after a disruption, meeting the availability expectations of its customers and {{frameworks}}.

## 2. Scope
This policy covers the people, processes, systems, and suppliers needed to deliver {{company_name}}'s critical services, including workloads on {{cloud_providers}}, and the backups and recovery capabilities that support them.

## 3. Business Impact and Objectives
{{company_name}} identifies its critical business processes and sets recovery objectives for each:
- **Recovery Time Objective (RTO)** — the maximum tolerable time to restore a service.
- **Recovery Point Objective (RPO)** — the maximum tolerable data loss, measured in time.
RTO and RPO targets are set by business owners, approved by {{approver}}, and reviewed annually.

## 4. Backup
- Critical data, including {{data_types}}, is backed up on a defined schedule consistent with its RPO.
- Backups are encrypted, access-controlled, and stored separately from the primary system (for {{cloud_providers}}, across regions or accounts where feasible).
- Backup restoration is tested at least annually to confirm backups are usable.

## 5. Resilience and Redundancy
Critical services use redundancy appropriate to their RTO, such as multi-zone or multi-region deployment on {{cloud_providers}}, so that the failure of a single component does not cause an extended outage.

## 6. Disaster Recovery Plan
{{company_name}} maintains a disaster recovery plan documenting how critical systems are recovered, who is responsible, how to invoke the plan, and how to communicate with staff, customers, and regulators during a major disruption.

## 7. Testing and Exercising
Continuity and recovery arrangements are tested at least annually through tabletop exercises or technical recovery tests. Results, gaps, and corrective actions are recorded and tracked to closure.

## 8. Roles and Responsibilities
- **{{approver}}** approves recovery objectives and authorises plan invocation for major events.
- **{{policy_owner}}** maintains this policy, the DR plan, and the test schedule.
- **System owners** implement backup and redundancy for their services.

## 9. Review
This policy and the supporting plans are reviewed at least annually, and after any major incident or significant change, by {{policy_owner}}.
