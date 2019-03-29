# Et tu, Brute?
#
# Chris Kalahiki
import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

DICT = open("dictionary.txt", "r")
DICT = DICT.read()
DICT = [i for i in DICT.split('\n')]

def encrypt(plaintext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return plaintext.translate(table)

def decrypt(ciphertext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return [i.translate(table) for i in ciphertext]

def isPlaintext(plaintext):
    match = 0
    for i in DICT:
        for k in plaintext:
            for j in k.split():
                if i == j: match += 1
    return True if match > 3 else False # This failed in at least 1 test case 

INPUT = sys.stdin.readlines()
for i in range(95):
    if isPlaintext(decrypt(INPUT, i)) == True:
        print("SHIFT=", i)
        for i in decrypt(INPUT, i): print(i.strip('\n'))
        break