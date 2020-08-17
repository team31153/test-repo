#!/usr/bin/env python3
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color('blue')
tess.right(180)
dist = 0
def spiral2(dist):
    
    for i in range(80):
        dist = dist + 5
        tess.forward(dist)
        tess.right(93)
def spiral1(dist):
    
    for i in range(80):
        dist = dist + 5
        tess.forward(dist)
        tess.right(90)
spiral1(dist)
wn.exitonclick()