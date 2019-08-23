#!/usr/local/bin/python
import os
import sys
import shutil


print("== ARGV ==")

for arg in sys.argv:
    print(f"{len(arg)}\t{arg}")


print("")
print("== ENVIRON ==")
for k, v in os.environ.items():
    print(f"{k}:\t{v}")

print("")
print("== STDIN ==")
shutil.copyfileobj(sys.stdin, sys.stdout)
sys.stdout.flush()
