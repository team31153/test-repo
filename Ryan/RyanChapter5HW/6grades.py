#!/usr/bin/env python3

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
print(len(xs))

for grade in xs:
    if grade >= 75:
        print("First")
    elif grade >= 70:
        print("Upper Second")
    elif grade >= 60:
        print("Second")
    elif grade >= 50:
        print("Third")
    elif grade >= 45:
        print("F1 Supp")
    elif grade >= 40:
        print("F2")
    else:
        print("F3")
