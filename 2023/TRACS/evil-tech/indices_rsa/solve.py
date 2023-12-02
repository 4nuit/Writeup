from Crypto.Util.number import *
from Crypto.PublicKey import RSA

f = open("public_key.pem","r").read()
key = RSA.importKey(f)
n = key.n; print(n)
e = key.e; print(e)
