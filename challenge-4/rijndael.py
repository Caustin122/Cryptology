# Rijndael
# by: The Epidemics

from sys import stdin
from hashlib import sha256, md5
from Crypto import Random
from Crypto.Cipher import AES
import base64
import re

# the AES block size to use
BLOCK_SIZE = 16
# the padding character to use to make the plaintext a multiple of BLOCK_SIZE in length
PAD_WITH = "#"
# the key to use in the cipher
#KEY = "rijndael"

# Dictionary Set-up
# dictionary = open('dictionary1-3.txt') # Insert dictionary file here
# word_list = dictionary.readlines()
# word_list = map(lambda s: s.strip().encode('utf-8'), word_list)

#with open('../hw6-aes/dictionary1-3.txt') as dictionary:
#    word_list = [line.strip() for line in dictionary]

# decrypts a ciphertext with a key
def decrypt(ciphertext, key):
	keyword = sha256(key.encode('utf-8')).digest()
	
	iv = md5(key.encode('utf-8')).digest()

	cipher = AES.new(keyword, AES.MODE_CBC, iv)
	
	plaintext = cipher.decrypt(base64.b64decode(ciphertext))

	# remove potential padding at the end of the plaintext
	# figure this one out...
	#plaintext = unpad(plaintext)

	return plaintext

# encrypts a plaintext with a key
# def encrypt(plaintext, key):
# 	# hash the key (SHA-256) to ensure that it is 32 bytes long
# 	key = sha256(key).digest()
# 	# generate a random 16-byte IV
# 	iv = Random.new().read(BLOCK_SIZE)

# 	# encrypt the ciphertext with the key using CBC block cipher mode
# 	cipher = AES.new(key, AES.MODE_CBC, iv)
# 	# if necessary, pad the plaintext so that it is a multiple of BLOCK SIZE in length
# 	plaintext += (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH
# 	# add the IV to the beginning of the ciphertext
# 	# IV is at [:16]; ciphertext is at [16:]
# 	ciphertext = iv + cipher.encrypt(plaintext)

# 	return ciphertext

# MAIN
word_list=["Your skills in C++"]
ciphertext = stdin.read().strip()
for key in word_list: # For valid words
    plaintext = decrypt(ciphertext, key)
    print("Plaintext: {}".format(plaintext))