#!/usr/bin/env python3
x = input("What was your mark")
x = int(x)

def grade(x):
    if x >= 75:
        print("First")
    elif x >= 70:
        print("Upper Second")
    elif x >= 60:
        print("Second")
    elif x >= 50:
        print("Third")
    elif x >= 45:
        print("F1 Supp")
    elif x >= 40:
        print("F2")
    if x < 40:
        print("F3")
grade(x)