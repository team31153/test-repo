#!/usr/bin/env python3
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