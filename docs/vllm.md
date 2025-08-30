# vLLM with Tensorized Models

[vLLM](https://github.com/vllm-project/vllm) can load tensorized weights
without conversion.

## Five‑Minute Quickstart

```bash
bash examples/vllm/run_vllm_tensorized.sh s3://my-bucket/models/tiny-gpt2.tensors
```

The script launches a server and performs a smoke test query.

## Fifteen‑Minute Deep Dive

1. `vllm serve --tensorizer` reads weights from disk, HTTP, or S3.
2. Environment variables like `VLLM_WORKER_GPU_MEMORY_UTILIZATION` tune
throughput vs. memory usage.
3. Prometheus metrics at `/metrics` expose time‑to‑first‑token and tokens/sec.
4. Scale out with KServe or plain Deployments using the Helm chart in
[`helm/tensorizer-vllm`](../helm/tensorizer-vllm/).

Refer to the [vLLM documentation](https://docs.vllm.ai/) for advanced options.
