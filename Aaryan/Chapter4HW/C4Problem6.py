#!/usr/bin/env python3
 
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(4)
tess.speed(5)
 
lengthOfTriangle = 150
 
  
def drawTriangle(t, sz):
   exterior = 360 / 3
   for i in range(3):
       t.forward(sz)
       t.right(120)
 
drawTriangle(tess, lengthOfTriangle)
 
wn.mainloop()
