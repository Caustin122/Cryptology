# Abraxas
#
# Chris Kalahiki

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

DICT = open("dictionary.txt", "r")
DICT = DICT.read()
DICT = [i for i in DICT.split('\n')]
DICT.reverse()

def encrypt(plaintext, key):
    shifted_alphabet = ''
    for char in key: 
        if char in ALPHABET: 
            if char not in shifted_alphabet: shifted_alphabet += char
    for char in ALPHABET: 
        if char not in shifted_alphabet: shifted_alphabet += char
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return plaintext.translate(table)

def decrypt(ciphertext, key):
    shifted_alphabet = ''
    for char in key: 
        if char in ALPHABET: 
            if char not in shifted_alphabet: shifted_alphabet += char
    for char in ALPHABET: 
        if char not in shifted_alphabet: shifted_alphabet += char
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return ciphertext.translate(table)

def isPlaintext(plaintext):
    match = 0
    for i in DICT:
        for j in plaintext.split():
            if i.lower() == j.lower(): match += 1
    return True if match > (len(plaintext)//5) else False

def validKey(key):
    for i in key:
        if key.count(i) > 1:
            return False
    return True

KEYS = [i for i in DICT if validKey(i) == True]

INPUT = input()
for i in KEYS:
    if isPlaintext(decrypt(INPUT, i)) == True:
        print("Key=", i, "\n", decrypt(INPUT, i))
        break

