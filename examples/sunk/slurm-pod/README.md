# Slurm Job Spawning a Kubernetes Pod

This example shows how a Slurm job can create a native Kubernetes Pod via the
`kubernetes` plugin.

## Prerequisites

- SUNK operator installed
- `kubectl` configured for the same cluster as Slurm

## Run

```bash
sbatch pod.sbatch
squeue -u $USER
kubectl get pods -l job-name=slurm-pod
```

Success criteria:

- `squeue` shows the job in `RUNNING`
- `kubectl get pods` shows the pod in `Running`
- `kubectl logs slurm-pod-0` prints `hello-world`

Clean up:

```bash
scancel <jobid>
```
