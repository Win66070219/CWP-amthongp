#!/usr/bin/env python

inp = input("Give me a number: ")

print(f"This number is an {'integer' if inp.isdecimal() else 'decimal'}.")