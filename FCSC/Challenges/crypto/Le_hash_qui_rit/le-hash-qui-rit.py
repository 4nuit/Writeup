import os
from hashlib import sha256

def SHA256(m):
    ctx = sha256()
    ctx.update(m)
    return ctx.digest()

def xor(A, B):
	return bytes([a ^ b for a, b in zip(A, B)])

N = 256
S = set()

challenge = os.urandom(32)
try:
	print(f"Input at most {N} messages M_i in hex format (empty line to exit) such that \\bigoplus_i SHA256(M_i) = 0x{challenge.hex()}")
	for _ in range(N):
		m = input(">>> ")
		if m == "": break
		S.add(bytes.fromhex(m))
except:
	print("Please check your inputs.")
	exit(1)

if len(S) == 0:
	print("You need to provide at least one input message.")
	exit(1)

r = b"\x00" * 32
for m in S:
	r = xor(r, SHA256(m))

if r == challenge:
	print(open("flag.txt").read())
else:
	print("Try again!")

