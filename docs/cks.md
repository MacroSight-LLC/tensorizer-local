# Security Notes

These guidelines align with the Kubernetes Certified Security Specialist (CKS)
objectives.

## Five‑Minute Quickstart

1. Apply the provided RBAC and NetworkPolicy manifests before deploying.
2. Use signed container images and verify SBOMs during admission.
3. Limit service accounts to the minimum required permissions.

## Fifteen‑Minute Deep Dive

- RBAC: see `security/policy-notes.md` for Role/RoleBinding examples.
- NetworkPolicies restrict pod egress to Object Storage and required services.
- Admission policies (OPA/Gatekeeper or Kyverno) enforce image signatures.
- Enable audit logging and ship logs to a secure location.

Security is continuous; integrate checks into CI/CD as shown in
[docs/cicd.md](cicd.md).
