# Rivets Arm His Lama Den
# Implements a simplistic RSA algorithm with the following characteristics:
# -expect input to contain the public key on the first line and a comma separated list of numbers representing encrypted values on the second line
# -the input provides n and e
# -write a function that determines if a number is prime
# -write a function that factors a number into the product of two primes
# -write a function that recursively calculates the greatest common divisor of a and b
# -write a function that naively calculates d, the modulo inverse of e
# -write a decrypt function that decrypts ciphertext C with the private key to get M
# -factor n as the product of two primes, p and q
# -calculate z = ((p - 1) * (q - 1)) / gcd(p - 1, q - 1)
# -calculate d as the inverse modulo of e
# -output the public and private keys
# -decrypt each value from the input using the private key to generate a valid ASCII character
# -rebuild the original message

from sys import stdin, stdout, stderr
from random import choice

MIN_PRIME = 100
MAX_PRIME = 999

# determines if a given number is prime
def isPrime(n):
    if (n % 2 == 0):
        return False
    for i in range (3, int(n ** 0.5 + 1), 2):
        if (n % i ==0):
            return False
    return True

# factors a number n into the product of two primes
def factor(n):
    for i in range(3,int(n**0.5+1),2):
        if (n%i == 0 and isPrime(i) and isPrime(n/i)):
            return i, n/i

# recursively returns the greatest common divisor of a and b
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# naively calculates the inverse modulo of e and z
def naiveInverse(e, z):
    d = 0
    while d < z:
        if e*d%z == 1:
            return d
        d += 1

# decrypts a ciphertext C with a private key K_priv to get M
def decrypt(C, K_priv):
    d = K_priv[0]
    n = K_priv[1]
    return (C % d) ** n

# MAIN
# get input
ciphertext = stdin.read().rstrip('\n').split('\n')


# grab the public key and ciphertext values
# isolate e and n from the public key
K_pub = eval(ciphertext[0])
C = ciphertext[1].split(',')
print(K_pub)
print(C)
e = K_pub[0]
n = K_pub[1]
stderr.write("Public key: {}\n".format(K_pub))

# factor n into p and q
p,q = factor(n)
stderr.write("p={}, q={}\n".format(p,q))
stderr.write("n={}\n".format(n))

# calculate z
z = ((p-1)*(q-1)/gcd(p-1,q-1))
stderr.write("z={}\n".format(z))
stderr.write("e={}\n".format(e))
# calculate d
d = naiveInverse(e,z)
stderr.write("d={}\n".format(d))

# generate the private key
K_priv = (d,n)
stderr.write("Private key: {}\n".format(K_priv))
stderr.flush()

# implement RSA for the specified input Cs
M = ""
for c in C:
    m = decrypt(int(c), K_priv)
    try:
        M += chr(m)
        stdout.write(chr(m))
        stdout.flush()
    except:
        stderr.write("\nError: invalid plaintext.\n")
        break
    
print
