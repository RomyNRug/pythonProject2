
import turtle
paper= turtle.Screen()
cheese = turtle.Turtle()
turtle.bgcolor("pink")
cheese.hideturtle()
cheese.speed(50)
for i in range(350):
    cheese.forward(i)
    cheese.right(98)

turtle.pensize(3)
turtle.speed(15)

manual= turtle.Turtle()
for i in range (4):
    manual.forward(100)
    manual.left(360/4)

meli= turtle.Turtle()
for i in range(4):
    meli.forward(100)
    meli.right(360/4)

cali= turtle.Turtle()
for i in range (4):
    cali.back(100)
    cali.right(360/4)

tori= turtle.Turtle()
for i in range (4):
    cali.back(100)
    cali.left(360/4)


paper.exitonclick()

#for i in range(6):
 #   for colours in ["light blue", "white", "yellow","cyan","magenta","red"]:
  #      turtle.color(colours)
   #     turtle.circle(100)
    #    turtle.left(10)


