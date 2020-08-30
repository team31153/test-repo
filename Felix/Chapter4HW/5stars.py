import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(10)
for i in range (5):
    for i in range(5):
        tess.right(144)
        tess.forward(100)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

wn.mainloop()