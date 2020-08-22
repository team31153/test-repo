import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
for i in range(5):
    tess.right(144)
    tess.forward(100)

wn.mainloop()