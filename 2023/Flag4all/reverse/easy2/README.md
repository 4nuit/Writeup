# Auteur

`K_lfa (BZHack / ESDAcademy)`

## Decompiler PYC

Comme vu dans le chall précédent avec strace, le `.exe` cache un `.pyc`

```bash
python pyinstxtractor.py chall.exe
```

## Flag

```bash
cd *extracted
strings * | grep 'FLAG{'
strings: Attention : « PYZ-00.pyz_extracted » est un répertoire
FLAG{BZH4ck_kn0w_Y0ur_P0rT}z
```
