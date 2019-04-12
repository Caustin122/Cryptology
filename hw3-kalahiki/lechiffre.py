# Le Chiffre
#
# by: The Epidemics

import sys
from itertools import cycle,starmap

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
#ALPHABET = " -,;:!?/.'"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ" # Alt Alphabet for ciphertext-3.txt

# import dictionary
DICT = open("dictionary.txt", "r")
DICT = DICT.read().rstrip('\n').split('\n')
#KEYDICT = [i for i in DICT if len(i) >= 18] # For ciphertext-3.txt
TESTDICT = [i.lower() for i in DICT]
INPUT = sys.stdin.read().rstrip('\n')

# Create the repeated key for length of ciphertext
def keyList(ciphertext, key):
    key = list(key) 
    if len(ciphertext) == len(key): 
        return(key) 
    else: 
        for i in range(len(ciphertext) - len(key)): 
            key.append(key[i % len(key)]) 
    return ''.join(key)

# Decrypt per character
def dec(c,k):
    return ALPHABET[(ALPHABET.index(c)-ALPHABET.index(k))%len(ALPHABET)] if (k in ALPHABET and c in ALPHABET) else c

# Full decrypt function
def decrypt(ciphertext, key):
    plaintext = []
    key = keyList(ciphertext, key)
    inc = 0
    for i in range(len(ciphertext)):
        plaintext.append(dec(ciphertext[i], key[inc]))
        if ciphertext[i] in ALPHABET: inc += 1 # Only increment when ciphertext character is in dictionary
    return ''.join(plaintext)

# Checking if plaintext is human-readable
def isPlaintext(plaintext):
    match, count = 0, 0
    for j in plaintext.split(' '):
        if j.lower().strip("`~!@#$%^&*()-_=+[{]}\|;:\",<.>/?") in TESTDICT: # Don't strip apostrophes because they are in the dict
            match += 1
        count += 1
    perc = float(match)/float(count) # percent correct = words matched / words checked
    #print('{} / {} = {}'.format(match,count,perc))
    return True if perc >= 0.8 else False # 0.9 in case there  are trailing apostrophes that I didn't catch

# Main Program
for i in DICT: # Replace with KEYDICT for ciphertext-3.txt
    if isPlaintext(decrypt(INPUT, i)) == True: # Decrypts the input based on the key, then check if the decrypted text is readable
        print("Key: ", i) # If so, print the key and decrypted text
        print(decrypt(INPUT, i))
        break # stop searching if you find a valid response
""" if isPlaintext(decrypt(INPUT, 'Byzantine')) == True: # Decrypts the input based on the key, then check if the decrypted text is readable
    print(decrypt(INPUT, 'Byzantine')) """
