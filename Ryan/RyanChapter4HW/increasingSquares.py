#!/usr/bin/env python3

import turtle
import time
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(7)
length1 = 0

def drawSquare(length):
    for i in range(4):
        pen.down()
        pen.forward(length)
        pen.left(90)
    pen.penup()
    pen.forward(-10)
    pen.right(90)
    pen.forward(10)
    pen.left(90)


for i in range(5):
    length1 = length1 + 20
    drawSquare(length1)


wn.mainloop()
