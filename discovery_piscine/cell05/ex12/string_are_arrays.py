#!/usr/bin/env python

import sys

if len(sys.argv) <= 1:
    print("none")
else:
    if "z" not in sys.argv[1]:
        print("none")
    else:
        for i in sys.argv[1]:
            if i == "z":
                print("z", end="")
