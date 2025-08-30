# Overview

This repository demonstrates a CoreWeave aligned stack for high performance model serving.
It combines **Slurm on Kubernetes (SUNK)**, **Tensorizer**, **vLLM**, and CoreWeave
observability to provide fast, reproducible, and secure deployments.

## Five‑Minute Quickstart

```bash
# clone and enter the repo
git clone https://github.com/coreweave/tensorizer
cd tensorizer

# run the Tensorizer demo
python examples/tensorizer/serialize_and_load.py --local-only
```

## Fifteen‑Minute Deep Dive

1. Deploy SUNK to a Kubernetes cluster and schedule a pod from a Slurm job.
2. Serialize and host a model using Tensorizer and CoreWeave Object Storage.
3. Launch vLLM pointing at the tensorized weights via the provided Helm chart.
4. Observe GPU and network metrics in CoreWeave Grafana dashboards.

The following documents provide more detail:

- [SUNK](sunk.md)
- [Schedule K8s Pods with Slurm](schedule-k8s-with-slurm.md)
- [Tensorizer](tensorizer.md)
- [vLLM](vllm.md)
- [Observability](observability.md)
- [CI/CD](cicd.md)
- [Security](cks.md)
