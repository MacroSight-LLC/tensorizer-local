"""Reproducible tensorizer serialization benchmark.

This harness creates a small synthetic ``torch.nn.Module`` and measures
serialization and deserialization speed using :mod:`tensorizer`.
It is intended to run offline on a single workstation and does not require
any external network access.

Example
-------

.. code-block:: bash

   python benchmarks/serialization_benchmark.py --layers 4 --hidden-size 256 --repeat 5

"""

from __future__ import annotations

import argparse
import tempfile
import time

import torch

from tensorizer import TensorDeserializer, TensorSerializer


def _build_model(layers: int, hidden_size: int, device: str) -> torch.nn.Module:
    """Create a simple feed‑forward network for benchmarking."""

    torch.manual_seed(0)
    modules = [torch.nn.Linear(hidden_size, hidden_size) for _ in range(layers)]
    model = torch.nn.Sequential(*modules).to(device)
    model.eval()
    return model


def run_benchmark(
    layers: int, hidden_size: int, device: str, repeat: int
) -> None:
    model = _build_model(layers, hidden_size, device)
    for i in range(repeat):
        with tempfile.NamedTemporaryFile() as fh:
            start = time.perf_counter()
            TensorSerializer(fh).write_module(model)
            fh.flush()
            ser_time = time.perf_counter() - start

            fh.seek(0)
            start = time.perf_counter()
            TensorDeserializer(fh).load_module(model)
            de_time = time.perf_counter() - start

            print(
                f"run={i} serialize={ser_time:.4f}s deserialize={de_time:.4f}s"
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--layers", type=int, default=2, help="number of linear layers"
    )
    parser.add_argument(
        "--hidden-size", type=int, default=128, help="width of each layer"
    )
    parser.add_argument("--device", default="cpu", help="device to run on")
    parser.add_argument("--repeat", type=int, default=3, help="number of runs")
    args = parser.parse_args()

    run_benchmark(args.layers, args.hidden_size, args.device, args.repeat)


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()
