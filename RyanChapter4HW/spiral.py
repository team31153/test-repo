#!/usr/bin/env python3

import turtle
import time
import random
wn = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(7)
angle = 90
size = 0
increase = 10
angle2 = 93
size2 = 0
increase2 = increase
R = 0
G = 0
B = 0

pen.penup()
pen.right(180)
pen.forward(200)
pen.right(180)
pen.down()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    pen.color(R,G,B)

def drawspiral1():

    global increase
    global angle
    global size
    for i in range(25):
        R = random.randrange(0, 257, 10)
        B = random.randrange(0, 257, 10)
        G = random.randrange(0, 257, 10)
        change_color()
        size = size + increase
        pen.right(angle)
        pen.forward(size)
        pen.right(angle)
        pen.forward(size)

def drawspiral2():

    global increase2
    global angle2
    global size2
    for i in range(25):
        R = random.randrange(0, 257, 10)
        B = random.randrange(0, 257, 10)
        G = random.randrange(0, 257, 10)
        change_color()
        size2 = size2 + increase2
        pen.right(angle2)
        pen.forward(size2)
        pen.right(angle2)
        pen.forward(size2)

drawspiral1()
distance = size / 2
distance = distance * -1
pen.penup()
pen.forward(-460)
pen.left(90)
pen.forward(distance)
pen.left(90)
pen.down()
drawspiral2()

wn.mainloop()
