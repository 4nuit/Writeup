#Non Résolu

from pwn import xor

k1 = b'1039380a3d3c0d0028465f0b3b016d704c1333193e7a12205a2d0812'
k2 = b'796a6d440c6a583705213558577159231276103c074e715469665a3c'
k3 = b'29011f095c24234c5654580723410665231874417a1e38121928237d'

passk1k2k3 = b'086744430f47467f12625875283534244866180b040a4e013176744e'

passwd = xor(xor(xor(passk1k2k3,k3),k2),k1); print("key4 = password", passwd.hex())

assert(xor(xor(xor(passwd,k1),k2),k3) == passk1k2k3)

cles = [k1, k2, k3, passwd]

for i in range(len(cles)):
	for j in range(i + 1, len(cles)):
		resultat = xor(cles[i], cles[j])
		print(f'key {i + 1} XOR key {j + 1}: {resultat}')
		#print(str(resultat)[2:-1])


