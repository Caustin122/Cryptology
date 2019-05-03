# Rijndael
# Sample template to show how to implement AES in Python

from sys import stdin
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import re

# the AES block size to use
BLOCK_SIZE = 16
# the padding character to use to make the plaintext a multiple of BLOCK_SIZE in length
PAD_WITH = "#"
# the key to use in the cipher
KEY = "rijndael"

# Dictionary Set-up
dictionary = open('dictionary1-3.txt')
word_list = dictionary.readlines()
word_list = map(lambda s: s.strip(), word_list)

# decrypts a ciphertext with a key
def decrypt(ciphertext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# get the 16-byte IV from the ciphertext
	# by default, we put the IV at the beginning of the ciphertext
	iv = ciphertext[:16]

	# decrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# the ciphertext is after the IV (so, skip 16 bytes)
	plaintext = cipher.decrypt(ciphertext[16:])

	# remove potential padding at the end of the plaintext
	# figure this one out...

	return plaintext

# encrypts a plaintext with a key
def encrypt(plaintext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# generate a random 16-byte IV
	iv = Random.new().read(BLOCK_SIZE)

	# encrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# if necessary, pad the plaintext so that it is a multiple of BLOCK SIZE in length
	plaintext += (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH
	# add the IV to the beginning of the ciphertext
	# IV is at [:16]; ciphertext is at [16:]
	ciphertext = iv + cipher.encrypt(plaintext)

	return ciphertext

# Frequency Check
def freq_check(plaintext):
    e_count, expected_frequency = 0, 0.1202
    candidate_text = plaintext
    adjusted_string = re.sub(r"[^a-z]", "", candidate_text.lower())
    for letter in adjusted_string:
        if letter == 'e':
            e_count += 1
    total_characters = len(adjusted_string)
    if e_count > 0:
        frequency = float(e_count / total_characters)
        confidence = (1 - float(abs(expected_frequency - frequency)) / float(expected_frequency))
        return confidence
    else:
        return 0

# MAIN
plaintext = stdin.read().rstrip("\n")
print ("Plaintext:")
print (plaintext)
print('\n')

ciphertext = encrypt(plaintext, KEY)
print ("Ciphertext (encrypted with {}):".format(KEY))
print (ciphertext)
print('\n')
print ("Ciphertext (encoded in base64):")
print (ciphertext.encode("base64").replace("\n", ""))
print('\n')

plaintext = decrypt(ciphertext, KEY)
print ("Plaintext (decrypted with {}):".format(KEY))
print (plaintext)
