# Rijndael

from sys import stdin
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import re

BLOCK_SIZE = 16
PAD_WITH = "#"
dictionary = open('dictionary.txt')
word_list = dictionary.readlines()
word_list = map(lambda s: s.strip(), word_list)


def decrypt(ciphertext, key):
    key = sha256(key).digest()
    print key
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    if len(ciphertext)%16 != 0:
        pad = (16 - len(ciphertext))%16
        while (pad > 0):
            ciphertext = ciphertext + "#"
            pad-=1
    plaintext = cipher.decrypt(ciphertext[16:])
    return plaintext


def encrypt(plaintext, key):
    key = sha256(key).digest()
    iv = Random.new().read(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext += (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH
    ciphertext = iv + cipher.encrypt(plaintext)
    return ciphertext


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
ciphertext = stdin.read().rstrip("\n")
for key in word_list:
    print key
    plaintext = decrypt(ciphertext, key)
    e_freq = freq_check(plaintext)
    if (e_freq >= .85) & (e_freq < 1):
        print plaintext
