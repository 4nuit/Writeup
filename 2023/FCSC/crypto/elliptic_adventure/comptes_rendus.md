﻿<a name="br1"></a>Challenge France Cybersécurité 2023

Comptes Rendus

Quentin Rataud

Avril 2023

1




<a name="br2"></a>Challenge France Cybersécurité 2023 Quentin R.

1 Les challenges

Elliptic Addventure

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951

b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)

E = EllipticCurve([K(a), K(b)])

mid = len(flag) // 2

Ax = K(bytes\_to\_long(flag[:mid]))

A = E.lift\_x(Ax)

print(f"{A + B = }")

Elliptic Addrenaline

p = 2\*\*255 - 19

a = 19298681539552699237261830834781317975544997444273427339909597334573241639236

K = GF(p)

E = EllipticCurve([K(a), K(b)])

mid = len(flag) // 2

Ax = K(bytes\_to\_long(flag[:mid]))

A = E.lift\_x(Ax)

print(f"{A + B = }")

2 of 7




<a name="br3"></a>Challenge France Cybersécurité 2023 Quentin R.

Deux points A et B sont présents sur une courbe elliptique d’équation

(E) : y2 = x3 + ax + b mod p

Dans le ﬁchier de sortie donné au candidat, les coordonnées des points A + B et A − B

` `Seules les équations des courbes et les coordonnées des points diﬀèrent entre les deux

2 Stratégie de résolution

` `Trouver 2 · A et 2 · B En connaissant ∇ = A + B et ∆ = A − B, il est facile d’en déduire

∇ + ∆ = (A + B) + (A − B)

∇ − ∆ = (A + B) − (A − B)

Cependant, retrouver A et B depuis 2 · A et 2 · B relève encore un peu de déﬁ.

2\.1 Elliptic Addventure

Propriétés des données Deux propriétés permettent de résoudre ce challenge sans diﬃculté.

• (E) est un groupe cyclique;

• L’ordre de (E) est un nombre premier.

Ces deux informations peuvent être vériﬁées grâce à un court code sage :

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951

b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)

E = EllipticCurve([K(a), K(b)])

print(E.gens())

\# ((38764697308493389993546589472262590866107682806682771450105924429005322578970 :

print(E.order())

\# 115792089210356248762697446949407573529996955224135760342422259061068512044369 # C'est un nombre premier !

3 of 7




<a name="br4"></a>Challenge France Cybersécurité 2023 Quentin R.

` `Vu que E.gens() retourne un tuple contenant un unique élément, (E) forme un groupe

k = E.order()

h = (k + 1) // 2

\# 57896044605178124381348723474703786764998477612067880171211129530534256022185

h est l’unique nombre tel que 2 · h = 1 mod k. En eﬀet, 2 · h = 1 + k.

Trouver A et B Étant donné que l’ordre de (E) est un nombre premier, tous les points

P · k = O

` `Cette propriété peut être utilisée pour retrouver les valeurs de A et B très rapidement

(2 · A) · h = A · (2 · h)

= A + A · k

B peut être retrouvé de manière identique.

4 of 7




<a name="br5"></a>Challenge France Cybersécurité 2023 Quentin R.

2\.2 Elliptic Addrenaline

Propriétés des données Premièrement, il est intéressant de constater que (E) forme

p = 2\*\*255 - 19

a = 19298681539552699237261830834781317975544997444273427339909597334573241639236

E = EllipticCurve([K(a), K(b)])

print(E.order())

\# 57896044618658097711785492504343953926856930875039260848015607506283634007912

print(E.gens())

\# ((17794503229134353635970439812949297100225489487588172568389327897754746546280 :

` `Vu que E.gens() retourne un tuple avec un unique élément G, la courbe elliptique est

Notons ensuite quelques propriété concernant A et B :

ordre = E.order()

\# 57896044618658097711785492504343953926856930875039260848015607506283634007912

\## Coordonnées des points données dans output.txt nabla = E(

36383477447355227427363222958872178861271407378911499344076860614964920782192, 26621351750863883655273158873320913584591963316330338897549941610801666281894, 1

) # = A + B

delta = E(

35017143636654127615837925410012912090234292410137109973033835965781971515338, 55888666729705323990488128732989325970476008697224551268788692630541877244410, 1

) # = A - B

aa = nabla + delta # = 2A

print(aa.order())

\# 28948022309329048855892746252171976963428465437519630424007803753141817003956

5 of 7




<a name="br6"></a>Challenge France Cybersécurité 2023 Quentin R.

print(bb.order())

\# 28948022309329048855892746252171976963428465437519630424007803753141817003956

` `Il est intéressant de constater que l’ordre de 2 · A et l’ordre de 2 · B est précisément 2

` `Finalement, il est important de noter que l’ordre de (E) est un multiple de 8, mais pas

k = ordre // 8 h = (k + 1) // 2

\# 3618502788666131106986593281521497120428558179689953803000975469142727125495

h est l’unique nombre tel que 2 · h = 1 mod k. En eﬀet, 2 · h = 1 + k.

Trouver A et B Soit G n’importe quel générateur de (E). Vu que (E) est cyclique d’ordre

8k, on sait que A = G · x pour un unique x entre 0 et 8k.

On possède 2 · A = G · (2x). Si nous multiplions ce point par h, nous obtenons

(2 · A) · h = G · (2hx)

Si par chance x est un multiple de 8, alors x = 8q pour un certain q. On obtient alors :

(2 · A) · h = G · (x + 8kq)

` `= (G · x) + (G · 8kq)

= A

` `On pourrait donc être tenté de générer des générateurs aléatoires de (E), d’espérer que

Supposons que x = 8q + r pour q, r entiers et 0 ≤ r < 8. Alors,

(2 · A) · h = G · (x + k(8q + r))

(2 · A) · h − G · kr = A

` `Tester les 8 diﬀérentes valeurs de r permet de retrouver la valeur de A à coup sûr. On

6 of 7




<a name="br7"></a>Challenge France Cybersécurité 2023 Quentin R.

3 Implémentation

3\.1 Elliptic Addventure

A = aa \* h

partie = long\_to\_bytes(int(A[0])) print(partie.decode(), end = '')

B = bb \* h

partie = long\_to\_bytes(int(B[0]))

\# FCSC{a0c43dbbfaac7a84b5ce7feb81d492431a69a214d768aa4383aabfd241}

3\.2 Elliptic Addrenaline

for r in range(8):

A = aa \* h - G \* k \* r

partie = long\_to\_bytes(int(A[0]))

for r in range(8):

B = bb \* h - G \* k \* r

partie = long\_to\_bytes(int(B[0]))

\# FCSC{1f0b8b8d4ff304004126f245ee5f46d8961b60dff4b187ef6fe4f09e34}

7 of 7