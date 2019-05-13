# Et tu, Brute?
# by: Chris Kalahiki
import sys
import base64
import string

# Hard-coded alphabet
#ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
#ALPHABET = "7JZv. 964jMLh)5QtAS2PXWaFU8,/cpkY'O(Tqr?dsEmbRwINVKBez1=3+H0GyfxCiD\"lg:!uo" # first alphabet
ALPHABET = "GHXJ+g5y6Asd3ZB4D12NT8mQEcarbSIo7zwjltOWu9eP/pFVL0KYqx=hRUCkviMf"
print("Len of Alphabet: " + str(len(ALPHABET)))
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
    table = string.maketrans(shifted_alphabet, ALPHABET)
    return [i.translate(table).decode("base64") for i in ciphertext]
    #return [i.translate(table) for i in ciphertext]

# Check for plaintext
def isPlaintext(plaintext):
    match, count = 0, 0
    for i in plaintext:
        for j in i.split():
            if j.lower().strip("`~!@#$%^&*()-_=+[{]}\|;:\",<.>/?") in DICT: match += 1
            count += 1
    perc = float(match)/float(count)
    return True if perc >= 0.5 else False # This failed in at least 1 test case 

#for i in range(95):
    #if isPlaintext(decrypt(INPUT, i)) == True:
print("SHIFT=", 27)
for i in decrypt(INPUT, 27): print(i)
