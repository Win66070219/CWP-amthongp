#!/usr/bin/env python

first_num = input("Give me the first number: ")
second_num = input("Give me the second number: ")

print("Thank you!")

arr = ["+", "-", "/", "*"]

for i in range(0, 4):
    print(f"{first_num} {arr[i]} {second_num} = {int(eval(first_num + arr[i] + second_num))}")