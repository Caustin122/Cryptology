# XOR ROX
# Sample template to show how to manipulate PNG pixels
# Also includes default values for the input and output image filenames
#  (keep them that way!)

from PIL import Image

# the images
INPUT_IMAGE = "input.png"
AND_IMAGE = "and.png"
OR_IMAGE = "or.png"
XOR_IMAGE = "xor.png"

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
print r, g, b
# change the current pipxel RGB values
pixels[row, col] = (0, 0, 0)

# get another pixel
row = 20
col = 20
r, g, b = pixels[row, col]
# display the current pixel RGB values
print r, g, b
# change the current pipxel RGB values
pixels[row, col] = (0, 0, 0)

# get another pixel
row = 30
col = 30
r, g, b = pixels[row, col]
# display the current pixel RGB values
print r, g, b
# change the current pipxel RGB values
pixels[row, col] = (0, 0, 0)

# write the new image
img.save(AND_IMAGE)

