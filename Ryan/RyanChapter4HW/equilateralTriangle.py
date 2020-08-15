#!/usr/bin/env python3

import turtle
import time
#from drawPolygonFunction import draw_poly
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(7)

length = 50

def draw_poly(t, n, sz):
    exteriorAngle = 360 / n
    interiorAngle = 360 - exteriorAngle
    for i in range(n):
        t.forward(sz)
        t.right(interiorAngle)

def draw_equitriangle(t, sz):
    draw_poly(pen, 3, length)

draw_equitriangle(pen, length)

wn.mainloop()
