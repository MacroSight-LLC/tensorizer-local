# Schedule Kubernetes Pods with Slurm

SUNK's `kubernetes` plugin allows a Slurm job to spawn a Kubernetes Pod.

## Five‑Minute Quickstart

```bash
# submit a job that launches a pod
sbatch examples/sunk/slurm-pod/pod.sbatch
squeue -u $USER
kubectl get pods -l job-name=slurm-pod
```

Expected output:

```
NAME          READY   STATUS    RESTARTS   AGE
slurm-pod-0   1/1     Running   0          1m
```

## Fifteen‑Minute Deep Dive

1. The `pod.sbatch` script uses `srun kubectl run` to create a pod.
2. Slurm cleans up the pod when the job completes.
3. Kubernetes RBAC controls what Slurm users may create.
4. Logs are visible through both `sacct` and `kubectl logs`.

To remove the pod:

```bash
scancel <jobid>
```
