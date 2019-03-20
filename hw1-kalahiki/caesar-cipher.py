# Et tu, Brute?
#
# Chris Kalahiki

# Alphabet goes here
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# Read in the dictionary.txt file
DICT = open("dictionary.txt", "r")
DICT = DICT.read()

# Encrypt plaintext based on provided shift number
def encrypt(plaintext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return plaintext.translate(table)

# Decrypt ciphertext based on provided shift number
def decrypt(ciphertext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return ciphertext.translate(table)

# Comparing with DICT to find real words
# Could be made to run more efficiently
def isPlaintext(plaintext):
    match = 0
    for i in DICT.split('\n'):
        for j in plaintext.split():
            if i == j:
                match += 1 # Counts number of matches in dictionary
    if match > 3:
        return True # If there are more than 3 words, this is probably plaintext
    else:
        return False

# Read in ciphertext, try all possible shifts, and return only those likely to be real plaintext
INPUT = input()
for i in range(95):
    if isPlaintext(decrypt(INPUT, i)) == True:
        print("SHIFT=", i, "\n", decrypt(INPUT, i)) # Print the candidates for correct plaintext

