#1
#response = [10, 8, 6, 4, 2]
#When step is negative this means that start must be bigger than stop

#2
import turtle
paper= turtle.Screen()
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
paper.exitonclick()
#In this case tess=alex is aliasing the two. If it were to say alex==tess than the two would not be equal to each other.

#3
a = [1, 2, 3]
b = a[:]
b[0] = 5
#snapshot: b is cloning a thus the snapshot should look similar to the book on page 116

#4
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))
#the reason why test 1 is false is becaused this and that are not aliasied with each other that is why in test 2 this = that is true

#5
summation_vector= 0
def add_vectors(vector1,vector2):
    for vector1,vector2 in add_vectors:
        sum_vector= vector1 + vector2
        summation_vectors=+ sum_vector
        print (summation_vector)
    return add_vectors

#6
def scalar_multi(scalar, vector):
    for scalar, vector in scalar_multi:
        scalar_multis= scalar*vector
    print("{0}","{1}", scalar_multis)

#7
def dot_product(vec1, vec2):
    for vec1, vec2 in dot_product:
        if vec1==vec2:
            sum_vec= vec1+vec2
    print(vec1,vec2, sum_vec)

#9
#when added "".join then the song will be spaced with a blank spac this makes it similar with the output of the song

#10
def myReplace(s,old,new):
    new.join(s.split(old))










