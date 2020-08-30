#!/usr/bin/env pybricks-micropython
ip = input('Enter your number:')
n = int(float(ip))
if n >= 75:
    print("first")
elif n >= 70 and n < 75:
    print("Upper second")
elif n >= 60 and n < 70:
    print("second")
elif n >= 50 and n < 60:
    print("third")
elif n >= 45 and n < 50:
    print(" F1 Supp")
elif n >= 40 and n < 45:
    print("F2")
else: 
    print("F3")