#!/usr/bin/env python3
"""Entry program for the-passport-page-of-a-countr-2-20261121-0318.

Copies the pre-generated passport spread (entry.png, drawn by gen_entry.py
with the Python standard library only) to the output directory.

SPDX-License-Identifier: MIT
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
