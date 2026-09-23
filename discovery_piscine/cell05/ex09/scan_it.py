#!/usr/bin/env python

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    matches = re.findall(f"{sys.argv[1]}", sys.argv[2])

    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))
