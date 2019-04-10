# Le Chiffre
#
# by: The Epidemics
import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "

# import dictionary
DICT = open("dictionary.txt", "r")
DICT = DICT.read()
DICT = [i for i in DICT.split('\n')]

INPUT = sys.stdin.readlines()
INPUT = [i.strip('\n') for i in INPUT]

def encrypt(plaintext, key):
    shifted_alphabet = ''
    # Add characters in key to beginning of shifted alphabet
    for char in key: 
        if (char in ALPHABET) and (char not in shifted_alphabet): shifted_alphabet += char
    # Add remaining characters in alphabet 
    for char in ALPHABET: 
        if char not in shifted_alphabet: shifted_alphabet += char
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return [i.translate(table) for i in plaintext]

def decrypt(ciphertext, key):
    shifted_alphabet = ''
    # Add characters in key to beginning of shifted alphabet
    for char in key: 
        if (char in ALPHABET) and (char not in shifted_alphabet): shifted_alphabet += char
    # Add remaining characters in alphabet 
    for char in ALPHABET: 
        if char not in shifted_alphabet: shifted_alphabet += char
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return [i.translate(table) for i in ciphertext]

#decrypt = lambda t,k,d=0:''.join([c,chr((ord(c)%32+ord(z)*(-1)**d+12)%26+1|ord(c)&96)][c.isalpha()]for c,z in zip(t,k*len(t)))

# Checking if plaintext is human-readable
def isPlaintext(plaintext):
    match, count = 0, 0
    for i in plaintext:
        for j in i.split():
            if j.lower().strip("`~!@#$%^&*()-_=+[{]}\|;:\",<.>/?") in TESTDICT: # Don't strip apostrophes because they are in the dict
                match += 1
            count += 1
    perc = float(match)/float(count) # percent correct = words matched / words checked
    return True if perc >= 0.9 else False # 0.9 in case there  are trailing apostrophes that I didn't catch

# Main Program
for i in DICT: # For each valid key in from the list
    if isPlaintext(decrypt(INPUT, i)) == True: # Decrypts the input based on the key, then check if the decrypted text is readable
        print("Key: ", i) # If so, print the key and decrypted text
        for i in decrypt(INPUT, i): print(i.strip('\n'))
        break # stop searching if you find a valid response

