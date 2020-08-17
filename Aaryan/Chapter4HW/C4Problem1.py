#!/usr/bin/env python3
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()      
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     
alex.color('hotpink')
alex.pensize(3)

for i in range(5):
    drawSquare(alex, 20)   
    alex.penup()
    alex.forward(40)      
    alex.pendown()

wn.exitonclick()