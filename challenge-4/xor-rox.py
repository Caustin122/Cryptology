# XOR ROX
# by: The Epidemics

from PIL import Image
from random import randrange

# the images
INPUT_IMAGE = "input.png"
XOR_IMAGE = "xor.png"

# get the input image
img = Image.open(INPUT_IMAGE)
pixels = img.load()
rows, cols = img.size

# Make a matrix of the appropriate size for the key
key = pixels

# Create a unique version of the image for the process
XOR = Image.open(INPUT_IMAGE)
XOR_pixels = XOR.load()

# XOR
for i in range(rows):
    for j in range(cols):
        XOR_pixels[i,j] = ((XOR_pixels[i,j][0] ^ key[i,j][0]) , (XOR_pixels[i,j][1] ^ key[i,j][1]) , (XOR_pixels[i,j][2] ^ key[i,j][2]))

# Save the modified image
XOR.save(XOR_IMAGE)