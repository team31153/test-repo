#!/usr/bin/env python3
x = input("What is the first leg of your triangle?")
x = int(x)
y = input("What is the second leg of your triangle?")
y = int(y)
def find_hypot(x, y):
    c = ((x**2)+(y**2))**0.5
    print(c)
find_hypot(x, y)
