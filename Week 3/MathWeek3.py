#1
for i in range(1000):
    print("I like turtles")

#2
month = ["January", "Febuary","March", "April","May", "June","July", "August", "September", "October", "November", "December" ]
for i in month:
    print("The month is ",month)

#3
import turtle
tess = turtle.Turtle()
paper= turtle.Screen
tess.left(3645)



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

john=turtle.Turtle()
for i in range(3):
    john.forward(100)
    john.left(120)


#Hexagon                    ocatgon is (forward 75 and left(360/8)

carlos=turtle.Turtle()
for i in range(6):
    carlos.forward(50)
    carlos.left(60)


#square


manual= turtle.Turtle()
for i in range (4):
    manual.forward(100)
    manual.left(360/4)


#6 +7 [160, -43, 270, -97, -43, 200, -940, 17,-86]

carbo= turtle.Turtle()
for angle in [160, -43, 270, -97, -43, 200, -940, 17,-86]:
    carbo.left(angle)
    carbo.forward(100)
print("The heading was", carbo.heading())


#8
#then in order to turn left should be 360/18=20 so 20 degrees


carbonara= turtle.Turtle()
carbonara.right(90)
carbonara.left(3600)
carbonara.right(-90)
carbonara.speed(10)
carbonara.left(3600)
carbonara.speed(0)
carbonara.left(3645)
carbonara.forward(-100)



#9

carbonara= turtle.Turtle()
for i in range(5):
    carbonara.forward(110)
    carbonara.left(216)
    carbonara.hideturtle()

#10

bolognese = turtle.Turtle()

bolognese.hideturtle()
bolognese.speed(20)
for i in range(350):
    bolognese.forward(i)
    bolognese.right(98)

#11


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



#1
numbers = (159, 26, 31, 416, 575, 65, 756, 81, 948)
count_odd = 0
count_even = 0
for x in numbers:
        if x % 2:
            count_odd+=1
        else:
            count_even+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#2
total=0
numbers = (159, 26, 31, 416, 575, 65, 756, 81, 948)
for i in numbers:
    total+=i
print(total)

#3
list = [-11,-116,-978,-616,-494,-161,-493]
total= 1
for i in list:
    if i < 0:
        total += i
print(total)

#4 ?????
list101= ["dance","scare","secret","chess","nice","expert", "sleep", "kettle"]
count=0
if len(list101) == 5:
    count+=1
print(count)

#5
numbers= [6,64.2,8,3,7,3]
sum = 0
for i in numbers:
        if i % 2 == 0:
           break
        else:
           sum += numbers

list= ["dance","scare","secret","chess","nice","expert", "sleep", "kettle"]

#6 Count how many words occur in a list up to and including the first occurrence of the word “sam”. (What if “sam” does not occur?)
list5=["carlos","juan","manuel","jason","marcos","sam"]
count=0
for i in list5:
    count += 1
    if i == ["sam"]:
        break


#7 Add a print function to Newton’s sqrt algorithm that prints out better each time it is calculated. Call your modified program with 25 as an argument and record the results
#do not understand the question?

#8

n=int(input("Please Enter n:"))
y1=((n**2)+n)/(2)
print (y1)










    



