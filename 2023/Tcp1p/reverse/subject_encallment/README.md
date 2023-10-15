## GDB

```bash
gdb -q ./chall
info functions
```

`0x0000000000001ba5  printFlag`


```bash
b *main
r
p *(char) printFlag()
```

`TCP1P{here_my_number_so_call_me_maybe}`
