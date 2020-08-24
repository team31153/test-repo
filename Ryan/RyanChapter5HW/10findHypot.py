#!/usr/bin/env python3

firstLength = int(input("Enter the length for the first side: "))
secondLength = int(input("Enter the length for the second side: "))
hypot = 0

def findHypo(f, s, h):
    f2 = f * f
    s2 = s * s
    h = f2 + s2
    h = h ** 0.5
    print(h)

findHypo(firstLength, secondLength, hypot)
