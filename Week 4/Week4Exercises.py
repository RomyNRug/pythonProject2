#1
def draw_square(hailey):
    for dummy in range(4):
        hailey.forward(20)
        hailey.left(90)
    hailey.penup()
    hailey.forward(50)
    hailey.pendown()
import turtle

hailey = turtle.Turtle()
hailey.color("Pink")
hailey.pensize(3)
bg = turtle.Screen()
bg.bgcolor("lightgreen")
for dummy in range(5):
    draw_square(hailey)
bg.mainloop()

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

bgg=turtle.Screen()
bgg.bgcolor("white")

brian=turtle.Turtle()
brian.color("yellow")
brian.pensize(2)

for i in range(5):
    draw_square(brian, 20 + 20 * i)

#3 Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like this:
def draw_poly(t,n,sz):
    for dummy in range (n):
        t.forward(sz)
        t.left(360/n)
tisha= turtle.Turtle()
tisha.color("aqua")
backg= turtle.Screen()

draw_poly(tisha,8,50)
backg.mainloop()



#4/6
def draw_poly(t, n, sz):
    for dummy in range(n):
        t.forward(sz)
        t.left(360 / n)
        t.speed(500)
mafia = turtle.Turtle()
mafia.color("blue")
mafia.pensize(2)
bag = turtle.Screen()
bag.bgcolor("lightgreen")
bag.title("Pretty")
for dummy in range(0, 20):
    draw_poly(mafia, 4, 100)
    mafia.right(18)

def equilatiral_triangle(t,sz):
    draw_poly(t,3,sz)
bag.mainloop()

#5
def square_spiral(ttl, trn, fwd):

    ttl.color("yellow")
    ttl.pensize(1)
    ttl.speed(500)
    ttl.penup()
    ttl.forward(fwd)
    ttl.pendown()
    for a in range(0, 100):
      ttl.forward(a * 2)
      ttl.right(trn)

bags = turtle.Screen()
bags.bgcolor("gray")
bags.title("Two spirals")

juanita = turtle.Turtle()
square_spiral(juanita, 90, -150)

octavio = turtle.Turtle()
square_spiral(octavio, 89, 150)
bags.mainloop()

#7
def sum_to(n):
    count=0
    for i in range(n+1):
        count=+ i
    return count

#8
def area_circle(r):
    pi= 3.14
    return pi*r**2

#9

paper=turtle.Screen()
def draw_star(ttl):
    for i in range(5):
        ttl.color("black")
        ttl.forward(100)
        ttl.left(144)

paper.exitonclick()

#10
def draw_pentagram(tori):
    tori.pendown()
    for x in range(5):
        tori.forward(100)
        tori.right(144)
    tori.penup()

backgorund= turtle.Screen()
backgorund.bgcolor("lightgreen")
tori = turtle.Turtle()
tori.color("HotPink")
tori.pensize(3)
tori.penup()

tori.backward(175)
tori.left(90)
tori.forward(60)
tori.right(90)
for dummy in range(5):
    draw_pentagram(tori)
    tori.forward(350)
    tori.right(144)
backgorund.mainloop()
