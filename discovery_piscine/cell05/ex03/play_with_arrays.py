#!/usr/bin/env python

ori_arr = [2, 8, 9, 48, 8, 22, -12, 2]

new_arr = set()

for i in range(len(ori_arr)):
    add_by_two = ori_arr[i] + 2
    if add_by_two > 5:
        new_arr.add(ori_arr[i] + 2)

print(ori_arr)
print(new_arr)