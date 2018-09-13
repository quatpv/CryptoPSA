from Crypto.Util.number import *
from fractions import gcd
import gmpy2
import random 
from ctf import secret

b = 1024

def gen_r():
	while True:
		r = random.randint(3, 2**(b/2)-1)
		if not r&1:
			return r

def gen_pq(r):
	while True:
		p = getPrime(b/2)
		q = getPrime(b/2)
		if gcd(p-1, r - 1) == 1 and gcd(q-1, r - 1) == 1:
			return (p, q)

def gen_key():
	r = gen_r()	
	(p, q) = gen_pq(r)
	N = p*q
	e = N - p - q + r	
	return (N, e, r)

def transform(byte, n, size):
	return (byte >> n) | ((byte & (((3 * (n * 2 + 1) & 1) << n) - (7 * (n * 2 + 1) & 1))) << (size - n))

def encrypt(secret):
	(N, e, r) = gen_key()
	size = 24
	c = 0L
	cipher = []
	for block in [secret[i:i + size] for i in range(0, len(secret), size)]:
		tmp = int(hex(c)[2:-1][:size*2+1], 16)
		x = random.randint(0, size - 1)
		if transform(ord(block[x]), x % 3, size)&1:
			c = pow(tmp + int(block.encode('hex'), 16), e, N)
		else:
			c = pow(tmp + int(block.encode('hex'), 16), r - 1, N)
		cipher.append(hex(c)[2:])

	with open('cipher.txt', 'w') as f:
		f.write('\n'.join(cipher))

encrypt(secret)