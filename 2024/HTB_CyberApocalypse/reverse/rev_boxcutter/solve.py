from pwn import xor

flag = xor(b"\x7f\x63\x75\x4c\x43\x45\x03\x54\x06\x59\x50\x68\x43\x5f\x04\x68\x54\x03\x5b\x5b\x02\x4a\x37",b"\x37")
print(flag)
