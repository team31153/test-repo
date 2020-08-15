#!/usr/bin/env python3

import turtle
import time
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(7)

def drawSquare():

    for i in range(4):
        pen.down()
        pen.forward(20)
        pen.left(90)
    pen.penup()
    pen.forward(40)


for i in range(5):
    drawSquare()

    
wn.mainloop()
