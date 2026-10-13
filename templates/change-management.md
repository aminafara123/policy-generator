# {{company_name}} Change Management Policy

> **Control mapping.** ISO/IEC 27001:2022 Annex A 8.32 (change management), 8.31 (separation of development, test & production), 8.9 (configuration management), 8.28 (secure coding) · SOC 2 CC8.1.

**Owner:** {{policy_owner}} · **Approver:** {{approver}} · **Classification:** Internal · **Applies to:** all {{company_name}} personnel who change production systems, and the systems themselves.

## 1. Purpose
This policy ensures changes to {{company_name}}'s systems and software are made in a controlled way that preserves the security, integrity, and availability of services and of {{data_types}}, in line with {{frameworks}}.

## 2. Scope
This policy applies to changes to production systems, applications, infrastructure, and security-relevant configuration across {{cloud_providers}} and on-premises environments, including code deployments, infrastructure changes, and configuration changes.

## 3. Change Principles
- All production changes are authorised, tested, and traceable to a request or ticket.
- Development, test, and production environments are separated, and production {{data_types}} are not used in lower environments without masking.
- Changes follow least-privilege: the person requesting a change should not be the sole approver of their own high-risk change (segregation of duties).

## 4. Change Types
- **Standard** — pre-approved, low-risk, repeatable changes that follow a documented procedure.
- **Normal** — changes that require review and approval before deployment.
- **Emergency** — urgent changes to restore service or fix a security issue, approved on an expedited basis and reviewed retrospectively.

## 5. Change Process
1. **Request** — the change is recorded with its purpose, scope, risk, and rollback plan.
2. **Review and approve** — an appropriate approver (not solely the author for high-risk changes) authorises the change.
3. **Test** — changes are tested, and code changes are peer-reviewed before merge.
4. **Deploy** — the change is deployed through a controlled, repeatable pipeline where possible.
5. **Verify** — the change is confirmed successful, or rolled back using the documented plan.

## 6. Emergency Changes
Emergency changes may bypass the normal approval queue to restore service or address a security issue, but are logged, communicated to {{policy_owner}}, and reviewed and formally approved after the fact.

## 7. Records and Traceability
Change records, approvals, test evidence, and deployment logs are retained so that who changed what, when, and with whose approval can be reconstructed for audit under {{frameworks}}.

## 8. Roles and Responsibilities
- **Change requesters** document and test their changes.
- **Approvers** assess risk and authorise changes.
- **{{policy_owner}}** maintains this policy and monitors change compliance.

## 9. Review
This policy is reviewed at least annually by {{policy_owner}} and approved by {{approver}}.
