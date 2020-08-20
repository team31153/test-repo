#!/usr/bin/env python3
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
def star(t, sz):
    tess.right(36)
    for i in range(5):
        t.forward(sz)
        t.left(144)
star(tess, 100)
tess.left(36)
