#!/usr/bin/env python3

import turtle
import random
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(7)
R = 0
G = 0
B = 0

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()


    pen.color(R,G,B)
for i in range(20):
    change_color()
    for i in range(4):

        pen.forward(150)
        pen.left(90)
    pen.right(18)

wn.mainloop()
