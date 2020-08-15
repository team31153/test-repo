#!/usr/bin/env python3

import turtle
import time
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(7)
sides = 8
length = 50

def draw_poly(t, n, sz):
    exteriorAngle = 360 / n
    interiorAngle = 360 - exteriorAngle
    for i in range(n):
        t.forward(sz)
        t.right(interiorAngle)

draw_poly(pen, sides, length)
wn.mainloop()
