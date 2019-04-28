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

# get the input image
img = Image.open(INPUT_IMAGE)
pixels = img.load()
rows, cols = img.size
print('[input.png is loaded]')

# Initialize the randomly generated key here
key = pixels
for i in range(rows):
    for j in range(10):
        key[i, j] = randrange(255), randrange(255), randrange(255)

def And():
    AND = pixels

    for i in range(rows):
        for j in range(cols):
            print(pixels[i,j])
            AND[i,j] = AND[i,j] = ((pixels[i,j][0] & key[i,j][0]) , (pixels[i,j][1] & key[i,j][1]) , (pixels[i,j][2] & key[i,j][2]))

    # write the new image
    img.save(AND_IMAGE)

def Or():
    OR = pixels

    for i in range(rows):
        for j in range(cols):
            print(pixels[i,j])
            OR[i,j] = ((pixels[i,j][0] & key[i,j][0]) , (pixels[i,j][1] & key[i,j][1]) , (pixels[i,j][2] & key[i,j][2]))

    # write the new image
    img.save(OR_IMAGE)

def Xor():
    XOR = pixels

    for i in range(rows):
        for j in range(cols):
            print(pixels[i,j])
            XOR[i,j] = ((pixels[i,j][0] & key[i,j][0]) , (pixels[i,j][1] & key[i,j][1]) , (pixels[i,j][2] & key[i,j][2]))

    # write the new image
    img.save(XOR_IMAGE)

# Main Program
And()
Or()
Xor()
print('[and.png, or.png, xor.png are all stored]')