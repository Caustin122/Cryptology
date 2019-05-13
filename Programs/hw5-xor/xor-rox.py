# XOR ROX
# by: The Epidemics

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

# Make a matrix of the appropriate size for the key
key = pixels

# Create a unique version of the image for each process
AND = Image.open(INPUT_IMAGE)
OR = Image.open(INPUT_IMAGE)
XOR = Image.open(INPUT_IMAGE)
AND_pixels = AND.load()
OR_pixels = OR.load()
XOR_pixels = XOR.load()

# AND, OR, and XOR all at once
for i in range(rows):
    for j in range(cols):
        key[i, j] = (randrange(255), randrange(255), randrange(255)) # Assign a random value for the key
        print(key[i,j]) # Print key value
        AND_pixels[i,j] = ((AND_pixels[i,j][0] & key[i,j][0]) , (AND_pixels[i,j][1] & key[i,j][1]) , (AND_pixels[i,j][2] & key[i,j][2]))
        OR_pixels[i,j] = ((OR_pixels[i,j][0] | key[i,j][0]) , (OR_pixels[i,j][1] | key[i,j][1]) , (OR_pixels[i,j][2] | key[i,j][2]))
        XOR_pixels[i,j] = ((XOR_pixels[i,j][0] ^ key[i,j][0]) , (XOR_pixels[i,j][1] ^ key[i,j][1]) , (XOR_pixels[i,j][2] ^ key[i,j][2]))

# Save the modified images
AND.save(AND_IMAGE)
OR.save(OR_IMAGE)
XOR.save(XOR_IMAGE)