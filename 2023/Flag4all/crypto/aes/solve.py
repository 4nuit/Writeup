from pwn import xor

"""
pt1 = aesdec(ct1) xor iv
pt2 = aesdec(ct2) xor ct1

aesdec(ct1) == aesdec(ct2)
"""

ciphertext = bytes(32)
plaintext = bytes.fromhex("15fd32c552b0965c13830645fae64b12c90873b780e4dfa4afe4f122d0178bf4")

p1 = plaintext[:16]; p2 = plaintext[16:]
c1 = ciphertext[:16]; c2 = ciphertext[16:]

iv = xor(xor(p1,p2),c1); print(iv.hex())
