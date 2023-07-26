import os

compiler = "nvcc"

compiler_path = ''
which = f"which {compiler}"
with os.popen(which) as pf:
    compiler_path = pf.readlines()[0]
    compiler_path = compiler_path.strip()

if not os.path.exists(compiler_path):
    print("nvcc not found, please check cuda env!")
    os.exit(-1)

compiler_path_b = f"{compiler_path}_b"

mv = f"mv {compiler_path} {compiler_path_b}"
os.system(mv)

nvcc_content ='''#!/usr/bin/env python
import sys, os
import subprocess

compiler = 'compiler_backup'
args = sys.argv[1:]
args.insert(0, f"{compiler}")
args.insert(1, "-ccbin=clang")

child = subprocess.Popen(args)
child.wait()
'''
nvcc_content = nvcc_content.replace('compiler_backup', compiler_path_b)


with open(compiler_path, "wt") as f:
    f.write(nvcc_content)

os.system(f'chmod 777 {compiler_path}')
