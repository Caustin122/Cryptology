# XOR ROX
# Sample template to show how to manipulate PNG pixels
# Also includes default values for the input and output image filenames
#  (keep them that way!)

from PIL import Image
from random import randrange

# the images
INPUT_IMAGE = "input.png"
AND_IMAGE = "and.png"
OR_IMAGE = "or.png"
XOR_IMAGE = "xor.png"

# Initialize the randomly generated key here

########## Everything above this line stays ##########

# get the input image
img = Image.open(INPUT_IMAGE)
pixels = img.load()
rows, cols = img.size

# pick some pixels to change
# get the current pixel
row = 10
col = 10
r, g, b = pixels[row, col]
# display the current pixel RGB values
print(r, g, b)
# change the current pipxel RGB values
pixels[row, col] = (0, 0, 0)

# get another pixel
row = 20
col = 20
r, g, b = pixels[row, col]
# display the current pixel RGB values
print(r, g, b)
# change the current pipxel RGB values
pixels[row, col] = (0, 0, 0)

# get another pixel
row = 30
col = 30
r, g, b = pixels[row, col]
# display the current pixel RGB values
print(r, g, b)
# change the current pipxel RGB values
pixels[row, col] = (0, 0, 0)

########## Everything below this line stays ##########

def And():
    # get the input image
    img = Image.open(INPUT_IMAGE)
    pixels = img.load()
    rows, cols = img.size

    for i in range(cols):
        for j in range(rows):
            # AND operation on key and input at this location
            print('AND')

    # write the new image
    img.save(AND_IMAGE)

def Or():
    # get the input image
    img = Image.open(INPUT_IMAGE)
    pixels = img.load()
    rows, cols = img.size

    for i in range(cols):
        for j in range(rows):
            # OR operation on key and input at this location
            print('OR')

    # write the new image
    img.save(OR_IMAGE)

def Xor():
    # get the input image
    img = Image.open(INPUT_IMAGE)
    pixels = img.load()
    rows, cols = img.size

    for i in range(cols):
        for j in range(rows):
            # XOR operation on key and input at this location
            print('XOR')

    # write the new image
    img.save(XOR_IMAGE)

# Main Program
And()
Or()
Xor()
