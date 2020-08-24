#!/usr/bin/env python3
print("ALL VALUES MUST BE DIFFERENT!")
firstSide = int(input("What is the length of the first side? "))
secondSide = int(input("What is the length of the second side? "))
thirdSide = int(input("What is the length of the third side? "))

def isRightTriangle(x, y, z):



    if x > y:
        if x > z:
            print("Hypot = first")
            hypot = x
            leg1 = z
            leg2 = y
        elif x < z:
            print("Hypot = third")
            hypot = z
            leg1 = x
            leg2 = y
    elif y > z:
        if y > x:
            print("Hypot = second")
            hypot = y
            leg1 = x
            leg2 = z
    elif x < y:
        if y < z:
            print("Hypot = third")
            hypot = z
            leg1 = x
            leg2 = y
        if y > z:
            print("Hypot = second")
            hypot = y
            leg1 = x
            leg2 = z
    else:
        print("Please try again. Remember, DIFFERENT NUMBERS")

    leg1sqr = leg1 * leg1
    leg2sqr = leg2 * leg2
    sum = leg1sqr + leg2sqr
    hypot2 = hypot * hypot

    if abs(sum-hypot2) < 0.000001:
        print("It is a right triangle")
    else:
        print("It is not a right triangle")

isRightTriangle(firstSide, secondSide, thirdSide)
