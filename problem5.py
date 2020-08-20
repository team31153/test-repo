#!/usr/bin/env python3
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.color('blue')
wn.bgcolor("lightgreen")
def spiral(d, a):
  for i in range(70):
        d = d+5
        tess.forward(d)
        tess.right(a)
spiral(0, 90)  