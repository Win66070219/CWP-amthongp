#!/usr/bin/env python

import sys

if len(sys.argv) <= 2:
    print("none")
else:
    for i in range(len(sys.argv) - 1, 0, -1):
        print(f"{sys.argv[i]}", end="\n")