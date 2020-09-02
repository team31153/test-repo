#!/usr/bin/env python3
import turtle

def drawBar(t, height):
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(20)
    t.write(str(height))
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)


def fillColor(t,height):
    if height >=200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    drawBar(t,height)


xs = [-48,-117,200,240,160,260,220, -10]
maxheight = max(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()
tess.pensize(3)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

for i in xs:
    fillColor(tess,i)

wn.exitonclick()