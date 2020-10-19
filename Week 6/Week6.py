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
