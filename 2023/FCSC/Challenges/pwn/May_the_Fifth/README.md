# May the Fifth

**Category** : pwn
**Points** : 449

Un utilisateur de `zForth` a, pour des raisons de performances, désactivé ASAN ainsi que `ZF_ENABLE_BOUNDARY_CHECKS`,
car selon lui "setjmp/longjmp est désactivé et c'est bien suffisant".
Saurez-vous le détromper en lisant le contenu du fichier contenant le flag ?

`nc challenges.france-cybersecurity-challenge.fr 2107`

* SHA256(`core.zf`) = `f545ff506acddf3bc3681c57e35f702c47a2ec67a129db6a903e08437bbd432f`
* SHA256(`ld-2.31.so`) = `1b5443523321793d3a710ad1705fdc82614463d80720fbbf4682421ebf2311f8`
* SHA256(`libc-2.31.so`) = `d101c9566a74fe6c6c635e51083bc96cd1295b3ece1d1a3f0171a3aa0498a59d`
* SHA256(`libm-2.31.so`) = `973520ce22ea040bb5c3378e2c9952de0349039c39cb06edb4e861c0303acc7f`
* SHA256(`zforth`) = `fa76a231cc48fd5387b56d85e7aeaa16e349d40dadf7beec4900b823d1d893b5`
* SHA256(`zforth-src.tgz`) = `d3a4b36d348ea3c856011e2d9a58a056bf0d7f3ad5617a93ac27896583e6b85f`

## Files : 
 - [core.zf](./core.zf)
 - [ld-2.31.so](./ld-2.31.so)
 - [libc-2.31.so](./libc-2.31.so)
 - [zforth](./zforth)
 - [zforth-src.tgz](./zforth-src.tgz)
 - [libm-2.31.so](./libm-2.31.so)


