# Abraxas
#
# Chris Kalahiki
import sys

# The hard-coded alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# Importing and sorting the dictionary
DICT = open("dictionary.txt", "r")
DICT = DICT.read()
DICT = [i for i in DICT.split('\n')]
#DICT.reverse()
INPUT = sys.stdin.readlines() # Read in the input

# The decryption function
def decrypt(ciphertext, key):
    shifted_alphabet = ''
    for char in key: 
        if (char in ALPHABET) and (char not in shifted_alphabet): shifted_alphabet += char
    for char in ALPHABET: 
        if char not in shifted_alphabet: shifted_alphabet += char
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return [i.translate(table) for i in ciphertext]

# Checking if plaintext is human-readable
def isPlaintext(plaintext):
    match, count = 0, 0
    for i in plaintext:
        for j in i.split():
            for k in DICT:
                if j.lower() == k.lower(): match += 1
            count += 1
    #return True if match > 3 else False
    perc = float(match)/float(count)
    return True if perc >= 0.5 else False

# Checking if a word from the dictionary is a valid key (no repeated letters)
def validKey(key):
    for i in key:
        if key.count(i) > 1:
            return False
    return True

# Creating a list of valid keys from the dictionary using the validKey function
KEYS = [i for i in DICT if validKey(i) == True]

# Main Program
for i in KEYS: # For each valid key in from the list
    if isPlaintext(decrypt(INPUT, i)) == True: # Decrypts the input based on the key, then check if the decrypted text is readable
        print("Key=", i, "\n", decrypt(INPUT, i)) # If so, print the key and decrypted text
        break # stop searching if you find a valid response
    print(i)
