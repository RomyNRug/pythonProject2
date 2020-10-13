#1
def draw_square(alex):
    for dummy in range(4):
        alex.forward(20)
        alex.left(90)
    alex.penup()
    alex.forward(50)
    alex.pendown()
import turtle

alex = turtle.Turtle()
alex.color("Pink")
alex.pensize(3)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
for dummy in range(5):
    draw_square(alex)
wn.mainloop()

#2
def draw_square(turtl,length):
    turtl.pendown()
    for dummy in range(4):
        turtl.forward(length)
        turtl.left(20)
    turtl.penup()
    turtl.backward(10)
    turtl.right(90)
    turtl.forward(10)
    turtl.left(90)
    turtl.pendown()

bg=turtle.Screen()
bg.bgcolor("white")
brian=turtle.Turtle()
brian.color("yellow")
brian.pensize(2)

for i in range(5):
    draw_square(brian, 20 + 20 * i)

#3



