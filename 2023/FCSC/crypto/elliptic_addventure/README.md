# Refait à partir du compte rendu (Poustouflan)

Note perso, première fois que je m'attaque aux ECC.

Utiliser une debian-like pour `sage`

```bash
sudo apt install sagemath
```

## Points

![](./enonce.png)

Deux points A et B sont présents sur une courbe elliptique d’équation $$(E) : y2 = x3 + ax + b[p]$$. E est un [groupe](https://www.bibmath.net/dico/index.php?action=affiche&quoi=./g/groupe.html) qui est de plus [fini](https://fr.wikipedia.org/wiki/Groupe_fini) comme Z/pZ pour RSA.

Dans le fichier `output.txt`, les coordonnées des points A + B et A − B sont indiqués. L’objectif est de retrouver les coordonnées des points A et B, qui chiffrent le flag.

On sait qu'on peut additionner les points dans ce groupe, le plus dur est d'inverser les coordonnées de A et B pour flag (pas de multiplication/division des coordonnées).
Une ébauche de script que j'ai abandonné est dans `old.py`.

## Inverser

On se sert de 2 propriétés:

- E est un groupe [**cyclique**](https://www.techno-science.net/glossaire-definition/Groupe-cyclique.html) (comme l'ensemble des permutations ou Z/pZ (si p premier))
- L’**ordre** de (E) , k, est un nombre **premier** (en gros pour un point P c'est le plus petit entier qui vérifie $$P^k = 0$$ où 0 est le point à l'infini)

k est premier donc son inverse h vérifie $$2h = 1+ k$$ : en fait on veut **diviser par 2** : on cherche l'inverse h tq $$2.h = 1 [k]$$

## Retrouver A et B:

Pour trouver les bytes correspondant à chaque moitié de flag, on peut `multiplier les points par l'inverse du groupe`. 
Tous les points du groupes sont **générateurs** car k est premier.

$$(2.A).h = A.(2.h) = A.(k + 1) = A.k + A = A$$

Comme on l'a dit on multiplie par l'inverse pour "inverser" la multiplication par 2 et retrouver A.

```python
from Crypto.Util.number import long_to_bytes
from sage.all import *

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)
E = EllipticCurve([K(a), K(b)])

A_plus_B = E(65355407912556110148433442581541116153096561277895556722873533689053268966181, 105815222725531774810979264207056456440531378690488283731984033593201027022521)
A_minus_B = E(103762781993230069010083485164887172361256204634523864861966420595029658052179, 76878428888684998206116229633819067250185142636730603625369142867437006615111)

aa = A_plus_B + A_minus_B #2A
bb = A_plus_B - A_minus_B #2B

k = E.order() #premier
h = (k + 1) // 2 #inverse de k dans E (modulo 2)

A = aa * h
partie = long_to_bytes(int(A[0]))
print(partie.decode(), end = '')
B = bb * h
partie = long_to_bytes(int(B[0]))
print(partie.decode())
```

![](./flag.png)
