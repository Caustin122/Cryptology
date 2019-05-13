# Le Chiffre
v=lambda t,k,d=0:''.join([c,chr((ord(c)%32+ord(z)*(-1)**d+12)%26+1|ord(c)&96)][c.isalpha()]for c,z in zip(t,k*len(t)))

