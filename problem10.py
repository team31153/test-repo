#!/usr/bin/env python3
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.color('blue')
wn.bgcolor("lightgreen")
def star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)
star(tess, 100)

def draw_star5():
        tess.forward(350)
        tess.right(144)

for i in range(5):
        star(tess, 100)
        tess.penup()
        draw_star5()
        tess.pendown()
