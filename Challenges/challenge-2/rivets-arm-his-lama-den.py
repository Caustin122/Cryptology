from sys import stdin, stdout
import re
import hashlib

def decrypt(ciphertext,d,e,n):                          #decrypt a character with a given key
    print("Trying e=%d\nd=%d"%(e,d))
    print("Public key: (%d, %d)\nPrivate key:(%d, %d)"%(e,n,d,n))
    for C in range(1,len(ciphertext)):
        m = int(ciphertext[C]) ** d % n
        try:
            stdout.write(chr(m))
        except:
            print("\nError: invalid plaintext.\n")
            print("---------------------------")
            break
        print("\n")

def isPrime(n):                                 #determine if a number is prime
    for i in range(3, int(n ** 0.5 + 1), 2):
        if (n % i == 0):return False
    return True

def factor(n):                                  #finds 2 prime factors of a number
    for i in range(3, int(n ** 0.5 + 1), 2):
        if (n % i == 0 and isPrime(i) and isPrime(n/i)):
            return i, n/i

def gcd(a,b):                                   #greatest common denominator
    if b==0:
        return a
    return gcd(b,a % b)

def modInverse(e,z):                            # Modulo Inverse
    d=0
    while d < z:
        if e*d%z == 1:
            return d
        d+=1

#   Main
####################################################################################
ciphertext = re.split('\n|,',stdin.read().rstrip('\n'))
n = eval(ciphertext[0])
p,q = factor(n)                                 #finds the factors of n
print("p = %d\nq = %d"%(p,q))
z = (p-1)*(q-1)                                 #calsulates z with p and q
print("z = %d"%(z))
for e in range(3,z,2):                           #loops through each possible e
    if (gcd(e,n) == 1) and (gcd(e,z) == 1):     #if the e is co prime with n and z
        print(gcd(e,n))
        print(gcd(e,z))
        d = modInverse(e,z)                     #calculates d using the modulo invers
        decrypt(ciphertext,d,e,n)
