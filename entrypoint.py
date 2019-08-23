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


for arg in sys.argv[1:]:
    if os.path.isfile(arg):
        print("")
        print(f"== FILE: {arg} ==")
        with open(arg, 'r') as fo:
            shutil.copyfileobj(fo, sys.stdout)


print("")
print("== STDIN ==")
shutil.copyfileobj(sys.stdin, sys.stdout)


sys.stdout.flush()
