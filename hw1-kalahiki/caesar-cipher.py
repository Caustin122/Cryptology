# Et tu, Brute?
#
# Chris Kalahiki

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
METHOD = 1
shift = 1

def encrypt(plaintext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return plaintext.translate(table)

def decrypt(ciphertext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(shifted_alphabet, ALPHABET)
    return ciphertext.translate(table)

def method1(plaintext):
    print("Method 1")
    return 0

def method2(plaintext):
    print("Method 2")
    return 0

INPUT = raw_input("Ciphertext: ")
METHOD = raw_input("Method: ")
if METHOD = 1:
    for i in range(95):
        out = method1(decrypt(INPUT, i))
else if METHOD == 2:
    for i in range(95):
        out = method2(decrypt(INPUT, i))
print(out)

