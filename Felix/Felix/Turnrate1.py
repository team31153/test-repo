import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(1.2)
tess.speed(10)
sz = 4
for i in range (50):
    for i in range(2):
        tess.right(90)
        tess.forward(sz)
        sz = sz + 2


wn.mainloop()