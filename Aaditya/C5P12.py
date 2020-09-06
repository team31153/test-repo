#!/usr/bin/env python3
a = input("What is the first side of your triangle?")
a = int(a)
b = input("What is the second side of your triangle?")
b = int(b)
c = input("What is the third side of your triangle?")
c = int(c)
def is_right(a, b, c):
    if a > b:
        if a > c:
            hypot = a
            l1 = b
            l2 = c
    if a > b:
        if a < c:
            hypot = c
            l1 = b
            l2 = a
    if b > a:
        if b > c:
            hypot = b
            l1 = a
            l2 = c
    if b > a:
        if b < c:
            hypot = c
            l1 = a
            l2 = b
    if c > a:
        if c > b:
            hypot = c
            l1 = a
            l2 = b
    else:
        print("Please pick a set of different numbers")
    if hypot == ((l1**2)+(l2**2))**0.5:
        print("Your triangle is right")
    else:
        print("Your triangle is not right")

is_right(a ,b ,c)



