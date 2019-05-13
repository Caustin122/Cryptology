# Rijndael
# by: The Epidemics

from sys import stdin
from hashlib import sha256, md5
from Crypto import Random
from Crypto.Cipher import AES
import base64
import re

BLOCK_SIZE = 16

with open('dictionary.txt') as dictionary:
    word_list = [line.strip() for line in dictionary]

def decrypt(ciphertext, key):
    keyword = sha256(key.encode('utf-8')).digest()
    iv = ciphertext[:16]
    cipher = AES.new(keyword, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[16:])
    #plaintext = plaintext.decode('utf-8')
    return plaintext

# MAIN
word_list=["thegourdisourshepherd$"]
ciphertext = stdin.buffer.read().strip()
for key in word_list:
    plaintext = decrypt(ciphertext, key)
    print(plaintext)