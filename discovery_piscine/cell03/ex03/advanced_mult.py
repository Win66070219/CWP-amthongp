#!/usr/bin/env python

i = 0
j = 0
arr = []

while i <= 10:
    print(f"Table de {i} : ", end="")

    while j <= 10:
        print(i * j, end=" ")
        j += 1

    print()
    i += 1
    j = 0