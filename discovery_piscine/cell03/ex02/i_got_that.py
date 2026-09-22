#!/usr/bin/env python

is_first_time = True

while True:
    if is_first_time:
        inp = input("What you gotta say? : ")
        is_first_time = False
    else:
        inp = input("I got that! Anything else? : ")

    if inp == "STOP":
        break
