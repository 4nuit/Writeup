## Notes  : non réussi

Note perso, première fois que je m'attaque aux ECC.

Utiliser une debian-like pour `sage`

```bash
sudo apt install sagemath
```

# Points

Nous avons dans output.txt les coordonnées des points `A+B` et `A-B`.
Il nous faut celles de `A` et `B` puis "inverser".

On sait que les opérations de type `Point Addition` sont transitives, le plus dur est d'inverser les coordonnées de A et B pour flag.
Voici une ébauche de script que j'ai abandonné:

```python
from Crypto.Util.number import long_to_bytes
from sage.all import *

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)
E = EllipticCurve([K(a), K(b)])

A_plus_B = (65355407912556110148433442581541116153096561277895556722873533689053268966181, 105815222725531774810979264207056456440531378690488283731984033593201027022521)
A_minus_B = (103762781993230069010083485164887172361256204634523864861966420595029658052179, 76878428888684998206116229633819067250185142636730603625369142867437006615111)

Ax = abs((A_plus_B[0] + A_minus_B[0])/2)
Bx = abs((A_plus_B[0] - A_minus_B[0])/2)

k = 1
while (p**k - 1) % E.order():
        k += 1

print(k)
```
