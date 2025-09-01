#!/usr/bin/env python
"""Serialize EleutherAI/gpt-neo-125M to a local tensor file."""

import torch
from transformers import AutoModelForCausalLM
from tensorizer import TensorSerializer

MODEL_NAME = "EleutherAI/gpt-neo-125M"
TENSOR_PATH = "gpt-neo-125M.tensors"

def main() -> None:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to(device)
    serializer = TensorSerializer(TENSOR_PATH)
    serializer.write_module(model)
    serializer.close()
    print(f"Serialized to {TENSOR_PATH}")

if __name__ == "__main__":
    main()
