# {{company_name}} Access Control Policy

> **Control mapping.** ISO/IEC 27001:2022 Annex A 5.15 (access control), 5.16 (identity management), 5.17 (authentication information), 5.18 (access rights), 8.2 (privileged access), 8.3 (information access restriction), 8.5 (secure authentication) · SOC 2 CC6.1, CC6.2, CC6.3.

**Owner:** {{policy_owner}} · **Approver:** {{approver}} · **Classification:** Internal · **Applies to:** all {{company_name}} personnel, contractors, and systems.

## 1. Purpose
This policy defines how {{company_name}} grants, manages, and revokes access to information and systems so that only authorised people and services can reach the data they need, in line with {{frameworks}}.

## 2. Scope
This policy covers access to all {{company_name}} systems and data, including {{data_types}}, hosted on {{cloud_providers}} and on-premises, and applies to user accounts, service accounts, and administrative access.

## 3. Access Control Principles
- Access is granted on the principles of **least privilege** and **need to know**.
- Every individual has a unique identity; shared or generic accounts are prohibited except where technically unavoidable and formally approved.
- Access rights follow a documented request, approval, and provisioning process.

## 4. Identity and Authentication
- Multi-factor authentication (MFA) is required for remote access, administrative access, and access to {{cloud_providers}} and systems handling {{data_types}}.
- Passwords meet {{company_name}}'s password standard (length, complexity, and screening against known-breached credentials) and are never shared.
- Authentication secrets (passwords, keys, tokens) are stored and transmitted only in protected form.

## 5. Provisioning and De-provisioning
- Access is requested by the person's manager and approved by the system or data owner before provisioning.
- Access is granted based on role. Joiners receive the baseline access for their role; movers have access adjusted to their new role; leavers have all access revoked promptly, targeting same-day revocation on termination.
- The de-provisioning process is tied to the HR leaver process so access does not outlive employment.

## 6. Privileged Access
- Administrative and privileged access is restricted to named individuals, granted only for as long as needed, and logged.
- Privileged actions are monitored, and privileged accounts use MFA and separate credentials from day-to-day accounts.

## 7. Access Reviews
Access rights, including privileged access, are reviewed at least every six months (and for systems handling {{data_types}}, at least quarterly) by the relevant system or data owner. Excess or stale access is removed and the review is recorded.

## 8. Roles and Responsibilities
- **{{policy_owner}}** owns this policy, the access standards, and the review schedule.
- **System and data owners** approve access and perform reviews.
- **Managers** request and confirm access for their teams.
- Report suspected unauthorised access to {{security_contact}}.

## 9. Review
This policy is reviewed at least annually by {{policy_owner}} and approved by {{approver}}.
