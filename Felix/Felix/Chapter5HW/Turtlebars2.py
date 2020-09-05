#!/usr/bin/env pybricks-micropython
import turtle
def draw_bar(t, height):
    if height > 0:
        """ Get turtle t to draw one bar, of height. """
        if height >= 200:
            tess.color("blue", "red")
        elif height >= 100:
            tess.color("blue", "yellow")
        elif height <100:
            tess.color("blue", "green")
        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height)
        t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()             # Added this line
        t.forward(10)
        t.pendown()

    else:
        tess.color("blue", "green")
        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height)
        t.penup()
        t.forward(-15)
        t.write("  "+ str(height))
        t.forward(15)
        t.pendown()
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()             # Added this line
        t.forward(10)
        t.pendown()
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)

xs = [48,117,200,-50,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()