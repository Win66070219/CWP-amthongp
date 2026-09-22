#!/usr/bin/env python

inp = input("")

for i in inp:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")
    else:
        print(i, end="")