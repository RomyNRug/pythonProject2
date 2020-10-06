#8

def triangle_numbers(n):
    for i in range(1, n + 1):
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))

triangle_numbers(5)

#9 Write a program which prints True when n is a prime number and False otherwise
# Program to check if a number is prime or not

num = 407

# To take input from the user
num = int(input("Enter a number: "))
if num > 1:
        for i in range(2, num):
                if (num % i) == 0:
                        print(num, "false")
                        break
        else:
                print(num, "True")

#10 Revisit the drunk pirate problem. This time, the drunk pirate makes a turn, and then takes some steps forward, and repeats this. Our social science student now records pairs of data: the angle of each turn, and the number of steps taken after the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)]. Use a turtle todraw the path taken by our drunk friend.

#import turtle
#paper=turtle.Screen()
#zubi= turtle.Turtle
#path = [160, -43, 270,-43]
#angle=[20,10,8,12]
#def draw_path(zubi,path,angle):
 #   for i in path,angle:
  #      zubi.left(angle)
   #     zubi.forward(path)

#11
#import turtle
#tori = turtle.Turtle
#paper = turtle.Screen()
#tori.left(100)

#12??????

#13
def num_digits(n):
    i=0
    count = 0
    while i < n:
        i+=1
        if n%2==0:
            count += 1
    return count

#14  Write a program that computes the sum of the squares of the numbers in the list numbers. For example a call with, numbers = [2, 3, 4] should print 4+9+16 which is 29.
list = [0,1,2,3,4,5,6]
for i in list:
        sqr= (i**2)
print("the number is {0} and the square is {1}".format(i,sqr))




