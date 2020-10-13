import turtle

def draw_multicolor_square(animal, size):
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)


def draw_rectangle(animal, width, height):
    for _ in range(2):
        animal.forward(width)
        animal.left(90)
        animal.forward(height)
        animal.left(90)

window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square
for _ in range(15):
    draw_multicolor_square(tess, size)
    size += 10 # Increase the size for next time
    tess.forward(10) # Move tess along a little
    tess.right(18)


def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
tess = turtle.Turtle()

draw_square(tess, 50)

window.mainloop()

def final_amount(p, r, n, t):
    a = p * (1 + r/n) ** (n*t)
    return a
toInvest = float(input("How much do you want to invest?"))
fnl = final_amount(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)

