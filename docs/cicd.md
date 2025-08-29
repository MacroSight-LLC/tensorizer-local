# CI/CD

This repository uses GitHub Actions to build, scan, and deploy containers.

## Five‑Minute Quickstart

1. Push changes to GitHub.
2. The workflow builds the image with `docker build` and scans it with Trivy.
3. If successful the image is pushed to the registry and Helm is upgraded in a
test namespace.

## Fifteen‑Minute Deep Dive

1. Workflows authenticate to the registry using OIDC and short‑lived tokens.
2. Secrets are provided via External Secrets and not committed to the repo.
3. The pipeline commits updated Helm chart values to a GitOps branch for ArgoCD.
4. Image tags are signed with Cosign and SBOMs are generated via Syft.

See [`.github/workflows/build-and-deploy.yml`](../.github/workflows/build-and-deploy.yml).
