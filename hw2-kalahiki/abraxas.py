# Abraxas
#
# Chris Kalahiki
#
# Includes encryption function for future use 

# Alphabet goes here
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# Read in the dictionary.txt file
DICT = open("dictionary.txt", "r")
DICT = DICT.read()

# Encrypt plaintext based on provided shift number
def encrypt(plaintext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift] # shift alphabet
    table = str.maketrans(ALPHABET, shifted_alphabet) # create mapping between alphabets
    return plaintext.translate(table) # use mapping to transform plaintext

# Decrypt ciphertext based on provided shift number
def decrypt(ciphertext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift] # shift alphabet
    table = str.maketrans(shifted_alphabet, ALPHABET) # create mapping between alphabets
    return ciphertext.translate(table) # use mapping to transform ciphertext

# Comparing with DICT to find real words
# Could be made to run more efficiently
def isPlaintext(plaintext):
    match = 0
    for i in DICT.split('\n'): # for each line in dictionary
        for j in plaintext.split(): # for each word in 'plaintext'
            if i == j: #if word matched dictionary entry
                match += 1 # Counts number of matches in dictionary
    if match > 3: # change this number for more or less leniancy on 'human-readable' check
        return True # If there are more than 3 words, this is probably plaintext
    else:
        return False # Else, probably not human-readable (or less than 4 words)

# Read in ciphertext, try all possible shifts, and return only those likely to be real plaintext
INPUT = input()
for i in range(95): # for each possible shift value
    if isPlaintext(decrypt(INPUT, i)) == True:
        print("SHIFT=", i, "\n", decrypt(INPUT, i)) # Print the candidates for correct plaintext
        break

