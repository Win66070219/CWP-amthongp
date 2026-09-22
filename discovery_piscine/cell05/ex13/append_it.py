#!/usr/bin/env python

import sys
import re

if len(sys.argv) <= 1:
    print("none")
else:
    for i in sys.argv[1:]:
        match = re.search(r"ism", i)

        if not match:
            print(i, end="ism\n")
