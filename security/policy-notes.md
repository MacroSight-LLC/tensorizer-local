# Security Policies

## RBAC Example

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-runner
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "get", "list"]
```

## NetworkPolicy Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: restrict-egress
spec:
  podSelector: {}
  policyTypes: [Egress]
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              access: object-storage
```

## Image Signing

Images are signed with [Cosign](https://github.com/sigstore/cosign).  Generate
SBOMs with [Syft](https://github.com/anchore/syft) and store them alongside the
images.  Admission controllers should verify signatures before allowing pods to
run.
