#!/usr/bin/env python

print("Enter a number less than 25")
inp = int(input(""))

if inp > 25:
    print("Error")
else:
    while inp <= 25:
        print(f"Inside the loop, my variable is {inp}")
        inp += 1