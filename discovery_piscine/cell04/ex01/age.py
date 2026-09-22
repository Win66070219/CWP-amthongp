#!/usr/bin/env python

inp = input("Please tell me your age: ")

print(f"You are currently {inp} years old.")

for i in range(0, 3):
    print(f"In {(i + 1) * 10} years, you'll be {int(inp) + ((i + 1) * 10)} years old.")