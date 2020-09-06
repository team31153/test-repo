#!/usr/bin/env python3
a = input("What is the first side of your triangle?")
a = int(a)
b = input("What is the second side of your triangle?")
b = int(b)
c = input("What is the third side of your triangle?")
c = int(c)
def is_right(a, b, c):
    if c == ((a**2)+(b**2))**0.5:
        print("Your triangle is right")
    else:
        print("Your triangle is not right")
is_right(a, b, c)

