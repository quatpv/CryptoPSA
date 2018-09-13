from Crypto.Util.number import *
from Crypto.PublicKey import *
import gmpy2
from secret import flag

p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 65537

psa = pow(2, p-0xcafebabe, n)
message = bytes_to_long(flag)
ciphertext = pow(message, e, n)
ciphertext = long_to_bytes(ciphertext)
ciphertext = ciphertext.encode("hex")

out_str = "[1] ciphertext: " + ciphertext + "\n[2] n: " + str(n) + "\n[3] e: " + str(e) + "\n[4] psa: " + str(psa)
f = open("data.txt",'w')
f.write(out_str)