import base64
from sys import stdin

ciphertext = stdin.read().strip()
print(base64.b64decode(ciphertext))