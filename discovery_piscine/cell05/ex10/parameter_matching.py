#!/usr/bin/env python

import sys

if len(sys.argv) < 2 or len(sys.argv) >= 3:
    print("none")
else:
    inp = input("What was the parameter? ")
    user_word = sys.argv[1]

    if inp == user_word:
        print("Good job!")
    else:
        print("Nope, sorry...")