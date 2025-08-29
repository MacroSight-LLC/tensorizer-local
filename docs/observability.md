# Observability

CoreWeave provides managed Grafana dashboards for metrics and logs.

## Five‑Minute Quickstart

1. Deploy the vLLM example with the Helm chart.
2. Open the Grafana URL from the CoreWeave console.
3. Navigate to **Kubernetes / Workloads / Pods** and filter by your namespace.

Check GPU utilization, memory, network throughput, and pod restarts while
invoking the model.

## Fifteen‑Minute Deep Dive

1. The `kube-state-metrics` and `node-exporter` dashboards show cluster health.
2. vLLM exports Prometheus metrics such as `vllm_engine_execution_time`.
3. Logs are collected via Loki; search by `app=vllm`.
4. For a local demo use the [`observability/` example](../examples/observability/grafana/README.md)
which spins up Prometheus and Grafana with Docker Compose.

Screenshots can be added to `docs/img/` for presentations.
