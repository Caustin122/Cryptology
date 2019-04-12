import hashlib, sys

m = 0xf56e21a65599a9391ffa07a3707ad15f29a7b63e9bddc919a0d4899f6a78a5314d142d57ae886fa98f84b2aa77bb79819397b1eb4b7e35820a80af08374c294c
f = open('dictionary.txt')
DICT = f.readlines()
DICT = [x.strip('\n') for x in DICT]

i = 0
while i <= len(DICT):
    x = hashlib.sha512(DICT[i])
    #if x==m:
    print(x)
    i += 1

