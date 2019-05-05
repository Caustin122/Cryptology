# Et tu, Brute?
# by: Chris Kalahiki
import sys

# Hard-coded alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# Importing dictionary and stdin to lists
DICT = open("dictionary.txt", "r")
DICT = DICT.read()
DICT = [i.lower() for i in DICT.split('\n')]
INPUT = sys.stdin.readlines()
INPUT = [i.strip('\n') for i in INPUT]

# Encrypt function
def encrypt(plaintext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return plaintext.translate(table)

# Decrypt function
def decrypt(ciphertext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return [i.translate(table) for i in ciphertext]

# Check for plaintext
def isPlaintext(plaintext):
    match, count = 0, 0
    for i in plaintext:
        for j in i.split():
            if j.lower().strip("`~!@#$%^&*()-_=+[{]}\|;:\",<.>/?") in DICT: match += 1
            count += 1
    perc = float(match)/float(count)
    return True if perc >= 0.9 else False # This failed in at least 1 test case 

for i in range(95):
    if isPlaintext(decrypt(INPUT, i)) == True:
        print("SHIFT=", i)
        for i in decrypt(INPUT, i): print(i.strip('\n'))
        break