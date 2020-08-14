#!/usr/bin/env python3

import turtle
import time
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(3)
length = 100
pen.right(180)
pen.penup()
pen.forward(250)
pen.right(180)
pen.down()

def drawStar(l):

    for i in range(5):
        pen.forward(l)
        pen.right(144)

def move():

    pen.penup()
    pen.forward(350)
    pen.right(144)
    pen.down()

for i in range(5):

    drawStar(length)
    move()

wn.mainloop()
