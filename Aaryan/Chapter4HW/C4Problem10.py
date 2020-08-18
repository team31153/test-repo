#!/usr/bin/env python3
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color('blue')
tess.pensize(3)
bruh = 100
def drawStar(t):
   for i in range(5):
       tess.forward(t)
       tess.right(144)
 
def next():
 
  
   tess.forward(350)
   tess.right(144)
  
 
for i in range(5):
 
   drawStar(bruh)
   next()
 
wn.mainloop()
