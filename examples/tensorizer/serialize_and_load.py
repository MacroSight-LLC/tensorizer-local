"""Serialize a tiny model, upload to S3 or serve over HTTP, and lazily load it.

This script downloads `sshleifer/tiny-gpt2`, tensorizes it, optionally uploads
it to an S3 bucket, and then demonstrates lazy loading with multiple readers.
"""

import argparse
import os
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import torch
from transformers import AutoModelForCausalLM

from tensorizer import TensorDeserializer, TensorSerializer


def serialize(model_id: str, out_path: str) -> None:
    model = AutoModelForCausalLM.from_pretrained(model_id)
    serializer = TensorSerializer(out_path)
    serializer.write_module(model)


def upload_to_s3(path: str, bucket: str, key: str) -> None:
    import boto3

    s3 = boto3.client("s3")
    s3.upload_file(path, bucket, key)


def serve_file(path: str, port: int) -> threading.Thread:
    directory = os.path.dirname(os.path.abspath(path))
    os.chdir(directory)
    server = ThreadingHTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return thread


def load(uri: str, device: str, num_readers: int) -> None:
    model = AutoModelForCausalLM.from_pretrained("sshleifer/tiny-gpt2")
    des = TensorDeserializer(
        uri, device=device, lazy_load=True, num_readers=num_readers
    )
    des.load_into_module(model)
    print("Loaded to", device)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local-only", action="store_true", help="do not start HTTP server"
    )
    parser.add_argument("--bucket", help="S3 bucket", default="")
    parser.add_argument("--key", help="S3 key", default="tiny-gpt2.tensors")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--num-readers", type=int, default=4)
    args = parser.parse_args()

    out_path = "tiny-gpt2.tensors"
    serialize("sshleifer/tiny-gpt2", out_path)

    if args.bucket:
        upload_to_s3(out_path, args.bucket, args.key)
        uri = f"s3://{args.bucket}/{args.key}"
    elif args.local_only:
        uri = out_path
    else:
        port = 8000
        serve_file(out_path, port)
        uri = f"http://localhost:{port}/{os.path.basename(out_path)}"

    load(uri, args.device, args.num_readers)


if __name__ == "__main__":
    main()
