# Slurm on Kubernetes (SUNK)

SUNK runs Slurm control and worker nodes inside Kubernetes Pods.  Slurm and
native Kubernetes workloads can share the same cluster while maintaining
isolation.

```
+-----------------------------+
| Kubernetes Cluster          |
| +-------------------------+ |
| | Slurm Controller Pod    | |
| +-------------------------+ |
| | Slurm Worker Pods       | |
| +-------------------------+ |
| | Native K8s Workloads    | |
| +-------------------------+ |
+-----------------------------+
```

## Five‑Minute Quickstart

```bash
# install SUNK operator
helm repo add sunk https://coreweave.github.io/sunk
helm install sunk sunk/sunk-operator

# submit a job
sbatch examples/sunk/slurm-pod/pod.sbatch
```

## Fifteen‑Minute Deep Dive

1. Control planes are deployed via GitOps (Argo CD or Flux).
2. Worker Pod counts scale dynamically based on Slurm queue depth.
3. Slurm's Kubernetes plugin can launch native Pods alongside batch jobs.
4. Metrics and logs are exported to CoreWeave's managed Grafana.

For a demo of creating a Kubernetes Pod from Slurm see
[examples/sunk/slurm-pod](../examples/sunk/slurm-pod/README.md).
