#!/usr/bin/env python3
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
def draw_poly(t, n, sz):
 for i in range(n):
   t.forward(sz)
   x = 180*(n-2)/n
   t.left(180-x)
def draw_triangle(t, sz):
    draw_poly(tess, 3, sz)
draw_triangle(tess, 50)