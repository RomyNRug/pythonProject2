
#import turtle
#paper= turtle.Screen()
#cheese = turtle.Turtle()
#cheese.hideturtle()
#cheese.speed(20)
#for i in range(350):
#    cheese.forward(i)
#    cheese.right(98)

#paper.exitonclick()



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
