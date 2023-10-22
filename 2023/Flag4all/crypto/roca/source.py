from sage.all import *
from Crypto.Util.number import getRandomNBitInteger, isPrime, bytes_to_long
from os import urandom


def primorial(n):
	M = 1
	p = 1
	for i in range(n):
		p = next_prime(p)
		M *= p
	return int(M)

def generatePrime():
	p = 0
	while not isPrime(p):
		k = getRandomNBitInteger(k_size)
		a = getRandomNBitInteger(a_size)
		p = k*M + pow(g, a, M)
	return p

def generateKey():
	n = 0
	while n.bit_length() != key_size:
		p = generatePrime()
		q = generatePrime()
		n = p*q
	return n


e = g = 65537
M = primorial(39)
order = Zmod(M)(g).multiplicative_order()
key_size = 512
k_size = key_size//2 - round(log(M, 2))
a_size = ceil(log(Zmod(M)(g).multiplicative_order(), 2))
assert k_size == 37 and a_size == 62
n = generateKey()

flag = "FLAG{" + urandom(12).hex() + "}"
m = bytes_to_long(flag.encode())
c = pow(m, e, n)
print("n =", n)
print("e =", e)
print("c =", c)
