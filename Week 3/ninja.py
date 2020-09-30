import turtle
from turtle import Turtle
from typing import Type

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.pensize(10)

window= turtle.Screen()
window.bgcolor("light gray")

colors = ['red','orange','green','blue','purple']

for element in range (12):
    leonardo.color(colors[element % len(colors)])
    leonardo.forward(50)
    leonardo.left(30)

size= 10

size= size + 3

dicaprio= turtle.Turtle()
dicaprio.shape("turtle")
dicaprio.forward(size)
dicaprio.left(120)
dicaprio.forward(80)
dicaprio.left(120)
dicaprio.forward(80)
dicaprio.left(120)








print(element)

paper.exitonclick()

