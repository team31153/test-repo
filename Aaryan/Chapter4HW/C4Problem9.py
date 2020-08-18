#!/usr/bin/env python3
import turtle
 
def drawStar(t):
   for i in range(5):
       t.forward(100)
       t.left(216)
 
alex = turtle.Turtle()
drawStar(alex)
