#1
for i in range(1000):
    print("I like turtles")

#2
month = ["January", "Febuary","March", "April","May", "June","July", "August", "September", "October", "November", "December" ]
for i in month:
    print("The month is ",month)

#3
#import turtle
#tess = turtle.Turtle()
#tess.left(3645)
#paper= turtle.Screen
#paper.exitonclick()


#4 a, b, c, d
numbers= [12,10,32,3,66,17,42,99,20]
for i in numbers:
    print(i)

numbers= [12,10,32,3,66,17,42,99,20]
for i in numbers:
    squared = (i ** 2)
    print("the number is {} and its square is {}".format(i,squared))

total=0
numbers= [12,10,32,3,66,17,42,99,20]
for i in numbers:
    total +=i
print(total)

product=1
numbers= [12,10,32,3,66,17,42,99,20]
for i in numbers:
    product *=i
    print(product)

#5 Equilateral Triangle
#import turtle
#paper=turtle.Screen()
#john=turtle.Turtle()
#for i in range(3):
  #  john.forward(100)
   # john.left(120)
#paper.exitonclick()

#Hexagon                    ocatgon is (forward 75 and left(360/8)
#import turtle
#paper=turtle.Screen()
#carlos=turtle.Turtle()
#for i in range(6):
 #   carlos.forward(50)
  #  carlos.left(60)
#paper.exitonclick()

#square
#import turtle
#paper=turtle.Screen()
#manual= turtle.Turtle()
#for i in range (4):
 #   manual.forward(100)
 #   manual.left(360/4)
#paper.exitonclick

#6 +7 [160, -43, 270, -97, -43, 200, -940, 17,-86]
#import turtle
#paper= turtle.Screen()
#carbonara= turtle.Turtle()
#for angle in [160, -43, 270, -97, -43, 200, -940, 17,-86]:
 #   carbonara.left(angle)
 #   carbonara.forward(100)
#print("The heading was", carbonara.heading())
#paper.exitonclick()

#8
#then in order to turn left should be 360/18=20 so 20 degrees

#import turtle
#paper= turtle.Screen()
#carbonara= turtle.Turtle()
#carbonara.right(90)
#carbonara.left(3600)
#carbonara.right(-90)
#carbonara.speed(10)
#carbonara.left(3600)
#carbonara.speed(0)
#carbonara.left(3645)
#carbonara.forward(-100)
#paper.exitonclick()


#9
#import turtle
#paper= turtle.Screen()
#carbonara= turtle.Turtle()
#for i in range(5):
#    carbonara.forward(110)
#    carbonara.left(216)
#    carbonara.hideturtle()
#paper.exitonclick()

#10
#import turtle
#paper= turtle.Screen()
#bolognese = turtle.Turtle()

#bolognese.hideturtle()
#bolognese.speed(20)
#for i in range(350):
 #   bolognese.forward(i)
 #   bolognese.right(98)
#paper.exitonclick()

#11
import turtle
paper=turtle.Screen()
risotto=turtle.Turtle()
for i in range(12):
    risotto.penup()
    risotto.forward(80)
    risotto.pendown()
    risotto.forward(10)
    risotto.penup()
    risotto.forward(30)
    risotto.stamp()
    risotto.backward(120)
    risotto.right(30)

risotto.stamp()
paper.exitonclick()





    



