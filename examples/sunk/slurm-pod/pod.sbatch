#!/bin/bash
#SBATCH --job-name=slurm-pod
#SBATCH --output=slurm-pod.log

srun kubectl run slurm-pod-0 --image=busybox --restart=Never --command -- sh -c 'echo hello-world; sleep 30'
