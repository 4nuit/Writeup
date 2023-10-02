## Android Kernel img

- use file

```bash
file dist
```

- google

- https://android.googlesource.com/platform/system/tools/mkbootimg/+/refs/heads/master/unpack_bootimg.py

```bash
python test.py  --boot_img dist
```

```bash
zcat ramdisk | cpio -idmv
```

- flag

`out/res/images/charger/battery_fail.png`

![](./battery_fail.png)
