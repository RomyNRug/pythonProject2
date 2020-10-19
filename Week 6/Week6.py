#.2f% is decimal points
# backslash means next character is part of the string

from PIL import Image
import numpy as np

im = Image.open("fruit_fade(3).png")
#\Users\Gebruiker\PycharmProjects\pythonProject2\Week 6
# convert the image to a numpy array called 'pix'
pix = np.array(im)
new_pix = []

for row in pix:
    # create a new list for each row of pixels in the image
    new_row = []
    for pixel in row:
        new_row.append(pixel + 100)  #add each converted pixel (here +100) to the new ro
    new_pix.append(new_row)
new_pix = np.array(new_pix).astype('uint8')
im2 = Image.fromarray(new_pix)
im2.show()

maximum = np.max(pix)
scale = 255.0/maximum
new_pix = []
for row in pix:
    new_row = []
    for pixel in row:
        new_row.append(pixel * scale)
    new_pix.append(new_row)
new_pix = np.array(new_pix).astype('uint8')

im2 = Image.fromarray(new_pix)
im2.show()


def fade_bw(image):
    pixels = np.array(image, dtype='uint8')
    new_pix = [[(sum(pixels[row, col]) / 7) for col in range(pixels.shape[1])] for row in range(pixels.shape[0])]
    new_image = Image.fromarray(np.array(new_pix, dtype='uint8'))
    new_image.show()

    return new_image


def fade_color(image):
    pixels = np.array(image, dtype='int8')

    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            pixels[row, col, 0] *= 0.5
            pixels[row, col, 1] *= 0.5
            pixels[row, col, 2] *= 0.5

    new_image = Image.fromarray(pixels)
    new_image.show()

    return new_image

im = Image.open("fruit.jpg")
im2 = fade_bw(im)
im2.save("fruit_fade.png", "PNG")


###########################

with open("test.txt", "w") as myfile:
    myfile.write("My first file written from Python\n")
    myfile.write("---------------------------------\n")
    myfile.write("Hello, world!\n")

with open("test.txt", "r") as my_new_handle:
    for the_line in my_new_handle:
        print(the_line, end="")

