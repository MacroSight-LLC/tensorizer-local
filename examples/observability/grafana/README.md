# Grafana Walkthrough

Open the CoreWeave Grafana instance and inspect the following dashboards while
running the vLLM demo:

- **Kubernetes / Compute / GPU** – `DCGM_FI_DEV_GPU_UTIL`, `DCGM_FI_DEV_FB_USED`
- **Kubernetes / Networking / Namespace** – `container_network_receive_bytes_total`
- **Loki Logs** – query `app=vllm`

For a local stack:

```bash
docker compose up -d
open http://localhost:3000
```

Tear down with `docker compose down`.
