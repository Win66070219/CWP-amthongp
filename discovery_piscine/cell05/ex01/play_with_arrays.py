#!/usr/bin/env python

ori_arr = [2, 8, 9, 48, 8, 22, -12, 2]

new_arr = []

for i in range(len(ori_arr)):
    new_arr.append(ori_arr[i] + 2)

print(f"Original array: {ori_arr}")
print(f"New array: {new_arr}")