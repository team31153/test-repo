#!/usr/bin/env python3
from C5P1 import day
i = input("When did you go on vacation")
i = int(i)
b = input("how long did you stay")
b = int(b)

def jail(i, b):
    x = i + b
    day(x)
jail(i, b)

