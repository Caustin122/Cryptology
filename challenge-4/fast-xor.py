ciphertext = open("puzzle_encrypted", "r")
key = ["010101101011011101110"]

def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

print(xor(ciphertext, key))