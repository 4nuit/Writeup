## UPX Packed

Le binaire utilise gtk4, à installer (sinon erreur). 
`strace` / `binary ninja` ne donnent pas grand chose. On regarde les strings et on voit **UPX**

```bash
sudo pacman -S gt4 upx
```

Il ne reste plus qu'à unpack et regarder les strings à nouveau:

```bash
upx -d packed
strings packed | grep HTB
```
