from os import urandom

def xor(msg, key):
	return bytes([char^key[i%len(key)] for i, char in enumerate(msg)])

flag = "FLAG{" + urandom(12).hex() + "}"
key = urandom(6)
ciphertext = xor(flag.encode(), key)
print(ciphertext.hex())
