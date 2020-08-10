#!/usr/bin/env python3
#Problem one
import turtle

def draw_square(t, sz):
   """Make turtle t draw a square of sz."""
   for i in range(4):
       t.color("hotpink")
       t.forward(sz)
       t.left(90)
def program(t, x):
  for i in range(x):
    draw_square(alex, 20)
    t.penup()
    t.forward(40)
    t.pendown()


wn = turtle.Screen()        
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()
program(alex, 5)            
wn.mainloop()
#problem 2
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color('hotpink')
def draw_square(t,size):
  for i in range(4):
    tess.forward(size)
    tess.left(90)

size = 20
for j in range(5):
  tess.pensize(3)
  draw_square(tess,size)
  size = size + 20
  tess.penup()
  tess.goto(tess.pos() + (-10, -10))
  tess.pendown()

wn.mainloop()
#problem 3
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
def draw_poly(t, n, sz):
 for i in range(n):
   t.forward(sz)
   x = 180*(n-2)/n
   t.left(180-x)
tess.color("hotpink")
draw_poly(tess, 8, 50) 
#Problem 4