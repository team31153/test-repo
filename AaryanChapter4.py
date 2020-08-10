#!/usr/bin/env python3
#Problem 1
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
#Problem 2
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
#Problem 3
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()       
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess, 8, 50)
#Problem 4
import turtle

def draw_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    alex = turtle.Turtle()
    alex.color("blue")
    alex.pensize(3)
    boxes = 20

    for _ in range(boxes):
        draw_square(alex, 200)
        alex.left(360 / boxes)

    wn.mainloop()
