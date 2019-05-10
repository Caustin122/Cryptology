# Add a space every 7 (or 8) characters
from sys import stdin

def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

ciphertext = stdin.read().strip()
print(encrypt(ciphertext, 8))