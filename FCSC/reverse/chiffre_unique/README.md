# Notes: non réussi

On peut utiliser Ghidra.

Pas mal de fonctions, notamment une avec un `SHA 256` générant le flag:

Le `main`:

```c

undefined8 FUN_001010a0(void)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  undefined8 uVar5;
  long lVar6;
  char *__s;
  undefined *puVar7;
  int iVar8;
  uint local_12c;
  undefined local_128 [256];
  
  iVar8 = 0;
  puVar7 = local_128;
  do {
    lVar6 = 0;
    do {
      __isoc99_scanf(&DAT_00102011,&local_12c);
      if (0xf < local_12c) {
        __s = "Invalid argument.";
        goto LAB_00101148;
      }
      puVar7[lVar6] = (char)local_12c;
      lVar6 = lVar6 + 1;
    } while (lVar6 != 0x10);
    iVar8 = iVar8 + 0x10;
    puVar7 = puVar7 + 0x10;
  } while (iVar8 != 0x100);
  uVar1 = FUN_00101255(local_128);
  uVar2 = FUN_001012a7(local_128);
  uVar3 = FUN_001012f2(local_128);
  uVar4 = FUN_0010136c();
  if ((uVar4 & uVar1 & uVar2 & uVar3) == 0) {
    __s = "Input incorrect.";
LAB_00101148:
    puts(__s);
    uVar5 = 1;
  }
  else {
    puts("Congratulations ! ");
    FUN_0010139d(local_128);
    uVar5 = 0;
  }
  return uVar5;
}
```

et la fonction appelée après Congratulations:

```c

void FUN_0010139d(void *param_1)

{
  byte *pbVar1;
  long lVar2;
  byte local_a8 [32];
  SHA256_CTX local_88;
  
  lVar2 = 0;
  SHA256_Init(&local_88);
  SHA256_Update(&local_88,param_1,0x100);
  SHA256_Final(local_a8,&local_88);
  printf("FCSC{");
  do {
    pbVar1 = local_a8 + lVar2;
    lVar2 = lVar2 + 1;
    printf("%02x",(ulong)*pbVar1);
  } while (lVar2 != 0x20);
  puts("}");
  return;
```
