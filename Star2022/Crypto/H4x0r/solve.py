#!/usr/bin.python2
from itertools import cycle

#1 cipher = plain ^ key
#3 cipher ^key = plain
#2 key = plain ^cipher
 
cipher="623b23a65f726871e1136e1772867b557c1db710577c1de31444781db7104c" #62
key="Star{" #5

cipher=cipher.decode('hex')
print(cipher)
cipher=[ord(i) for i in cipher]
key=[ord(i) for i in key]

plain_key = [ t[0]^t[1] for t in zip(cipher,key)]	
key = [chr(x) for x in plain_key]
print("key:", ''.join(key))

for i in range(5,62):
	plain_key.append(plain_key[i%5])

plain = [t[0]^t[1] for t in zip(cipher,plain_key)]
plain = [chr(x) for x in plain]
print(''.join(plain))
