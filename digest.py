#!/usr/bin/env python3
import hashlib
import sys

if len(sys.argv) != 2:
    print("Usage: python3 digest.py <file>")
    sys.exit(1)

file_path = sys.argv[1]
with open(file_path, "rb") as f:
    data = f.read()
    digest = hashlib.sha256(data).hexdigest()

print(f"SHA256 Digest for {file_path}:\n{digest}")
