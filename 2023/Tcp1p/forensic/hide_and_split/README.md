## NTFS

## Montage disque

```bash
sudo mount -o ro,loop challenge.ntfs /mnt/test
```

Ne donne rien

## PNG

On récupère toutes les strings en hexa et supprime le texte: fichier `test`
On voit un header PNG.

```bash
xxd -r -p test > test.png
```

## Flag

https://zxing.org/w/decode

`TCP1P{hidden_flag_in_the_extended_attributes_fea73c5920aa8f1c}`
