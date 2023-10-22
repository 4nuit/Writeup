from Crypto.Util.number import getStrongPrime, bytes_to_long
from os import urandom

p = getStrongPrime(1024)
q = getStrongPrime(1024)
r = getStrongPrime(1024)
n = p*q*r
e = 65537
flag = "FLAG{" + urandom(12).hex() + "}"
m = bytes_to_long(flag.encode())
c = pow(m, e, n)
print("n =", n)
print("p =", p)
print("q =", q)
print("e =", e)
print("c =", c)
