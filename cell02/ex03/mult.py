#!/usr/bin/env python

print("Enter the first number:")
inp = int(input(""))

print("Enter the second number:")
inp2 = int(input(""))

result = inp * inp2

print(f"{inp} x {inp2} = {result}")

if result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("The result is positive.")