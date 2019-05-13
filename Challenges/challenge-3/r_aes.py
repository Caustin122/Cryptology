#############################
# Rijndael
# John Spurgeon, Marc Kliebert, Peyton Sidders, Grant Larson
# 04/30/19
# Python version of my AES decryption script
#############################

import re
from sys import stdin
from hashlib import sha256
from Crypto.Cipher import AES

# Debug constant
DEBUG = False
# Dictionary to use for keywords. Alternate dictionary
# commented out for easy swapping. This code can use the
# original 99,000 word dictionary just fine, if you'd like
DICTIONARY = "dictionary.txt"
# DICTIONARY = "dictionary1-3.txt"
# DICTIONARY = "dictionary4.txt"

# Read in ciphertext as a byte array
ciphertext = stdin.buffer.read().strip()
# Set initailization vector as the first 16 bytes
iv = ciphertext[:16]

# Read in keyword list from dictionary
with open(DICTIONARY) as dict_file:
    keyword_list = [line.strip() for line in dict_file]

# Debug printing
if DEBUG:
    print("ciphertext:\n" + ciphertext)
    print("initialization vector:\n" + iv)
    print("peak at key_word list:\n", keyword_list[:20])

# First, each keyword is hashed using sha256. Then a test
# cipher is created using the hashed key, CBC mode, and
# the initialization vector. It is important to create a
# separate cipher for testing, as the iv changes on each
# round of CBC. The test is performed by decrypting the
# first 32 bytes of the ciphertext, and attempting to
# read as a set of unicode characters. On error, the function
# returns None, which tells the "main" below not to print
# or break. On success, a new cipher is created from the
# original iv, and the entire ciphertext is decrypted and
# decoded into utf-8. The errors are ignored in case there
# is a tricky half-plain text in the challenge on friday.
# the trailing padding is removed and the plaintext is
# returned for printing.
def attack(key_word):
    key = sha256(key_word).digest()
    cipher_test = AES.new(key, AES.MODE_CBC, iv)
    plaintext_test = cipher_test.decrypt(ciphertext[16:48])
    try:
        plaintext_test.decode("utf-8")
    except UnicodeDecodeError:
        return None
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[16:])
    plaintext = re.sub('#+$', '', plaintext.decode("utf-8", errors="ignore"))
    return plaintext

# Iterates over keyword list, and if the plaintext
# is returned, it is printed, and the loop is broken.
for key_word in keyword_list:
    plaintext = attack(key_word.encode('utf-8'))
    if plaintext:
        print("KEY=" + key_word + ":")
        print(plaintext)
        break
