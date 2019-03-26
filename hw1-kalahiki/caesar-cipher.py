# Et tu, Brute?
#
# Chris Kalahiki

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
    return ciphertext.translate(table)

def isPlaintext(plaintext):
    match = 0
    for i in DICT:
        for j in plaintext.split():
            if i == j: match += 1
    return True if match > 3 else False # This failed in at least 1 test case

#def isEnglish(plaintext):       

INPUT = input()
for i in range(95):
    if isPlaintext(decrypt(INPUT, i)) == True:
        print("SHIFT=", i, "\n", decrypt(INPUT, i))
        break

