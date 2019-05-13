import hashlib
dictionary = open("text1.txt").readlines()
Hash = "f56e21a65599a9391ffa07a3707ad15f29a7b63e9bddc919a0d4899f6a78a5314d142d57ae886fa98f84b2aa77bb79819397b1eb4b7e35820a80af08374c294c"
for i in dictionary:
    i = i.rstrip("\n")
    Phash = hashlib.sha512(i).hexdigest()
    if Phash == Hash:
        print i
