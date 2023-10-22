#!/usr/bin/python3
from itertools import cycle
import string

#1 cipher = plain ^ key
#3 cipher ^key = plain
#2 key = plain ^cipher

charset = string.printable
for e in charset:
	cipher="889a67aab9bbfce644dca4bcf8e311dfa3bfade115def7eeaab31089f3f1"
	key="FLAG{"+e
	print(key,cipher)
	cipher = bytes.fromhex(cipher)
	cipher = [b for b in cipher]
	key = [ord(c) for c in key]

	plain_key = [ t[0]^t[1] for t in zip(cipher,key)]
	key = [chr(x) for x in plain_key]
	print("key:", ''.join(key))

	for i in range(len(key),len(cipher)):
        	plain_key.append(plain_key[i%len(key)])

	plain = [t[0]^t[1] for t in zip(cipher,plain_key)]
	plain = [chr(x) for x in plain]
	if plain[-1] == '}':
		print("FLAG: ", ''.join(plain))
		break
