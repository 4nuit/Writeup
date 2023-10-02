`main` appelle en cas de réussite `print_flag`

## Méthode 1

Reverse statique avec ghidra

```bash
gcc solve.c -o solve && ./solve
```

## Méthode 2

```bash
gdb -q ./build/8ball
b *main
r
p *(char) print_flag()
```

```bash
gdb-peda$ p *(char) print_flag()
bctf{Aw_$hucK$_Y0ur3_m@k1Ng_m3_bLu$h}
Cannot access memory at address 0x27
```
