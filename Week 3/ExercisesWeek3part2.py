#6
def grade(x):
    grade = ["First", "Upper Second", "Second", "Third", "F1 Supp", "F2", "F3"]

    if 75 <= x:
        return grade[0]
    elif 70 <= x and x <= 75:
        return grade[1]
    elif 60 <= x and x < 70:
        return grade [2]
    elif 50 <= x and x < 60:
        return grade [3]
    elif 45 <= x and x < 50:
        return grade [4]
    elif 40 <= x and x < 45:
        return grade [5]
    elif x < 40 :
        return grade[6]

from math import sqrt
a=5
b=10
c = sqrt((5**2)+(10**2))
print("the length of the right angle triangle is",c)

#8 do not get it, looked it up online, #9 too.

rightangled = float
input= (rightangled)
def rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
#9
def rightangled(a, b, c):
    if a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    elif b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

#10

import math
k = math.sqrt(2.0)
print(k, k*k)
print(k*k == 2.0)








