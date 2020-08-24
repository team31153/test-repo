#!/usr/bin/env python3
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:

        t.color("blue", "red")

        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height)
        t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()             # Added this line
        t.penup()
        t.forward(10)
        t.down()

    elif height >= 100:

        t.color("blue", "yellow")

        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height)
        t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()             # Added this line
        t.penup()
        t.forward(10)
        t.down()

    elif height >= 0:

        t.color("blue", "green")

        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height)
        t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()             # Added this line
        t.penup()
        t.forward(10)
        t.down()

    else:
        t.color("blue", "green")

        t.begin_fill()           # Added this line
        t.write("  "+ str(height))
        t.left(90)
        t.forward(height)
        #t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()             # Added this line
        t.penup()
        t.forward(10)
        t.down()

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)
tess.penup()
tess.right(180)
tess.forward(300)
tess.left(90)
tess.forward(200)
tess.left(90)
tess.down()

xs = [48,117,-45,200,240,160,260,220,-30]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
