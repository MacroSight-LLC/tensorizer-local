#!/usr/bin/env python
"""Deserialize tensors and generate text with gpt-neo-125M."""

import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer
from tensorizer import TensorDeserializer
from tensorizer.utils import no_init_or_tensor

MODEL_NAME = "EleutherAI/gpt-neo-125M"
TENSOR_PATH = "gpt-neo-125M.tensors"

def main() -> None:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    config = AutoConfig.from_pretrained(MODEL_NAME)
    with no_init_or_tensor():
        model = AutoModelForCausalLM.from_config(config, torch_dtype=torch.float16)
    deserializer = TensorDeserializer(TENSOR_PATH)
    deserializer.load_into_module(model)
    deserializer.close()
    model.to(device)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    inputs = tokenizer("Hello", return_tensors="pt").to(device)
    model.eval()
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=12)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()
