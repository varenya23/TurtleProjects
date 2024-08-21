import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colours=["red", "yellow", "blue", "green", "purple", "orange"]
for i in range(100):
    t.pencolor(colours[i%6])
    t.forward(i*2)
    t.left(62)
turtle.done()