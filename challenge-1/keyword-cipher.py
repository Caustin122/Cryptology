# Abraxas 
# by: Chris Kalahiki
#
# NOTE: If you want to reverse alphabet, uncomment line 16
import sys

# The hard-coded alphabet
#ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
#ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ" # For ciphertext-3.txt
#ALPHABET = "7JZv. 964jMLh)5QtAS2PXWaFU8,/cpkY'O(Tqr?dsEmbRwINVKBez1=3+H0GyfxCiD\"lg:!uo" # First alphabet
ALPHABET = "1234567890"

# Importing and sorting the dictionary
DICT = open("dictionary.txt", "r")
DICT = DICT.read()
DICT = [i for i in DICT.split('\n')] # Original dictionary
TESTDICT = [i.lower() for i in DICT] # Edited dictionary for testing if plaintext is readable
#DICT.reverse() # Reverse alphabet if needed
INPUT = sys.stdin.readlines() # Read in the input
INPUT = [i.strip('\n') for i in INPUT] # Strip newline characters

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

# The decryption function
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

# Checking if plaintext is human-readable
def isPlaintext(plaintext):
    match, count = 0, 0
    for i in plaintext:
        for j in i.split():
            if j.lower().strip("`~!@#$%^&*()-_=+[{]}\|;:\",<.>/?") in TESTDICT: # Don't strip apostrophes because they are in the dict
                match += 1
            count += 1
    perc = float(match)/float(count) # percent correct = words matched / words checked
    return True if perc >= 0.5 else False # 0.9 in case there  are trailing apostrophes that I didn't catch

# Checking if a word from the dictionary is a valid key (no repeated letters)
def validKey(key):
    if len([i for i in key]) == len(set(key)): # Lists allow repeats and sets don't =D
        return True
    return False

# Creating a list of valid keys from the dictionary using the validKey function
KEYS = [i for i in DICT if i.startswith("d") if validKey(i) == True]



# Main Program
""" for i in KEYS: # For each valid key in from the list
    print(i) # For debugging: Uncomment if you want to see where you are in the list of keywords
    if isPlaintext(decrypt(INPUT, i)) == True: # Decrypts the input based on the key, then check if the decrypted text is readable
        print("Key=", i) # If so, print the key and decrypted text
        for i in decrypt(INPUT, i): print(i.strip('\n'))
        break # stop searching if you find a valid response """
for i in encrypt(INPUT, "27"): print(i.strip('\n'))