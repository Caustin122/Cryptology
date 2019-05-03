# XOR ROX
# by: The Epidemics

from PIL import Image
from random import randrange
from sys import stdin
import csv

# the images
INPUT_IMAGE = "view-me.png"
XOR_IMAGE = "xor.png"

# get the input image
img = Image.open(INPUT_IMAGE)
pixels = img.load()
rows, cols = img.size

# Make a matrix of the appropriate size for the key
key = pixels
with open('key.txt') as keyfile:
    #csv_reader = csv.reader(keyfile, delimiter=',')
    key = [line.strip().split(',') for line in keyfile]
    #print(key)

#print(key)
""" for i in range(rows):
    for j in range(cols):

with open('key.txt') as key:
    csv_reader = csv.reader(key, delimiter=',')
    print(csv_reader)
key = csv_reader """
# Create a unique version of the image for each process
XOR = Image.open(INPUT_IMAGE)
XOR_pixels = XOR.load()

# AND, OR, and XOR all at once
k = 0
for i in range(rows):
    for j in range(cols):
        #key[i, j] = (randrange(255), randrange(255), randrange(255)) # Assign a random value for the key
        #print(key[i,j]) # Print key value
        XOR_pixels[i,j] = ((XOR_pixels[i,j][0] ^ int(key[k][0])) , (XOR_pixels[i,j][1] ^ int(key[k][1])) , (XOR_pixels[i,j][2] ^ int(key[k][2])))
        k += 1

# Save the modified images
XOR.save(XOR_IMAGE)