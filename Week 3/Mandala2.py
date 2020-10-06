import turtle

turtle.bgcolor("pink")
turtle.pensize(3)
turtle.speed(15)

for i in range(6):
    for colours in ["light blue", "white", "yellow","cyan","magenta","red"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
