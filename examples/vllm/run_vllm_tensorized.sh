#!/usr/bin/env bash
# Launch vLLM pointing at a tensorized model and run a smoke test.
set -euo pipefail

MODEL_URI=${1:-s3://my-bucket/models/tiny-gpt2.tensors}
PORT=${PORT:-8000}

vllm serve --model "$MODEL_URI" --tensorizer --port "$PORT" &
SERVER_PID=$!

sleep 5
curl -sS http://localhost:$PORT/generate -d '{"prompt":"Hello","max_tokens":8}'

kill $SERVER_PID
