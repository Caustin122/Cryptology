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


with open('dictionary.txt') as dictionary:
    word_list = [line.strip() for line in dictionary]

# decrypts a ciphertext with a key
def decrypt(ciphertext, key):
	keyword = sha256(key.encode('utf-8')).digest()
	iv = ciphertext[:16] #md5(key.encode('utf-8')).digest()
	cipher = AES.new(keyword, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext[16:]) #cipher.decrypt(base64.b64decode(ciphertext))
	return plaintext

# MAIN
word_list=["thegourdisourshepherd$"]
ciphertext = stdin.buffer.read().strip()
for key in word_list:
    plaintext = decrypt(ciphertext, key)
    #if '5447' in plaintext:
    print(plaintext)