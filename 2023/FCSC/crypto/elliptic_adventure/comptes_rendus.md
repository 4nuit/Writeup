<a name="br1"></a>Challenge France Cybersécurité 2023

Comptes Rendus

Quentin Rataud

Avril 2023

1




<a name="br2"></a>Challenge France Cybersécurité 2023 Quentin R.

1 Les challenges

Elliptic Addventure

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951a = -3

b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)

E = EllipticCurve([K(a), K(b)])

mid = len(flag) // 2

Ax = K(bytes\_to\_long(flag[:mid]))Bx = K(bytes\_to\_long(flag[mid:]))

A = E.lift\_x(Ax)B = E.lift\_x(Bx)

print(f"{A + B = }")print(f"{A - B = }")

Elliptic Addrenaline

p = 2\*\*255 - 19

a = 19298681539552699237261830834781317975544997444273427339909597334573241639236b = 55751746669818908907645289078257140818241103727901012315294400837956729358436

K = GF(p)

E = EllipticCurve([K(a), K(b)])

mid = len(flag) // 2

Ax = K(bytes\_to\_long(flag[:mid]))Bx = K(bytes\_to\_long(flag[mid:]))

A = E.lift\_x(Ax)B = E.lift\_x(Bx)

print(f"{A + B = }")print(f"{A - B = }")

2 of 7




<a name="br3"></a>Challenge France Cybersécurité 2023 Quentin R.

Deux points A et B sont présents sur une courbe elliptique d’équation

(E) : y2 = x3 + ax + b mod p

Dans le ﬁchier de sortie donné au candidat, les coordonnées des points A + B et A − Bsont indiqués. L’objectif est de retrouver les coordonnées des points A et B, qui encodent la solution des challenges.

` `Seules les équations des courbes et les coordonnées des points diﬀèrent entre les deuxchallenges.

2 Stratégie de résolution

` `Trouver 2 · A et 2 · B En connaissant ∇ = A + B et ∆ = A − B, il est facile d’en déduireles coordonnées de 2 · A et de 2 · B:

∇ + ∆ = (A + B) + (A − B) = 2 · A

∇ − ∆ = (A + B) − (A − B) = 2 · B

Cependant, retrouver A et B depuis 2 · A et 2 · B relève encore un peu de déﬁ.

2\.1 Elliptic Addventure

Propriétés des données Deux propriétés permettent de résoudre ce challenge sans diﬃculté.

• (E) est un groupe cyclique;

• L’ordre de (E) est un nombre premier.

Ces deux informations peuvent être vériﬁées grâce à un court code sage :

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951o = 115792089210356248762697446949407573529996955224135760342422259061068512044369a = -3

b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)

E = EllipticCurve([K(a), K(b)])

print(E.gens())

\# ((38764697308493389993546589472262590866107682806682771450105924429005322578970 :# 112597290425349970187225006888153254041358622497584092630146848080355182942680 :# 1),)

print(E.order())

\# 115792089210356248762697446949407573529996955224135760342422259061068512044369 # C'est un nombre premier !

3 of 7




<a name="br4"></a>Challenge France Cybersécurité 2023 Quentin R.

` `Vu que E.gens() retourne un tuple contenant un unique élément, (E) forme un groupe cyclique. L’ordre de E est un nombre premier que nous appelerons k par la suite. k étant premier, il possède alors un inverse modulaire modulo 2, et il est possible decalculer cet inverse :

k = E.order()

h = (k + 1) // 2

\# 57896044605178124381348723474703786764998477612067880171211129530534256022185

h est l’unique nombre tel que 2 · h = 1 mod k. En eﬀet, 2 · h = 1 + k.

Trouver A et B Étant donné que l’ordre de (E) est un nombre premier, tous les pointsde la courbe en sont des générateurs. Ceci implique que pour tout point P dans E,

P · k = O

` `Cette propriété peut être utilisée pour retrouver les valeurs de A et B très rapidementdepuis les valeurs de 2 · A et 2 · B :

(2 · A) · h = A · (2 · h) = A · (1 + k)

= A + A · k = A + O = A

B peut être retrouvé de manière identique.

4 of 7




<a name="br5"></a>Challenge France Cybersécurité 2023 Quentin R.

2\.2 Elliptic Addrenaline

Propriétés des données Premièrement, il est intéressant de constater que (E) formeégalement un groupe cyclique. Cependant, cette fois-ci, son ordre n’est pas un nombrepremier. Il est possible de prouver ceci et de trouver un générateur de la courbe elliptiquesimplement grâce à un court code sage :

p = 2\*\*255 - 19

a = 19298681539552699237261830834781317975544997444273427339909597334573241639236b = 55751746669818908907645289078257140818241103727901012315294400837956729358436K = GF(p)

E = EllipticCurve([K(a), K(b)])

print(E.order())

\# 57896044618658097711785492504343953926856930875039260848015607506283634007912

print(E.gens())

\# ((17794503229134353635970439812949297100225489487588172568389327897754746546280 :# 17671033459111968710988296061676524036652749365424210951665329683594356030064 :# 1),)

` `Vu que E.gens() retourne un tuple avec un unique élément G, la courbe elliptique estcyclique et G en est un générateur.

Notons ensuite quelques propriété concernant A et B :

ordre = E.order()

\# 57896044618658097711785492504343953926856930875039260848015607506283634007912

\## Coordonnées des points données dans output.txt nabla = E(

36383477447355227427363222958872178861271407378911499344076860614964920782192, 26621351750863883655273158873320913584591963316330338897549941610801666281894, 1

) # = A + B

delta = E(

35017143636654127615837925410012912090234292410137109973033835965781971515338, 55888666729705323990488128732989325970476008697224551268788692630541877244410, 1

) # = A - B

aa = nabla + delta # = 2Abb = nabla - delta # = 2B

print(aa.order())

\# 28948022309329048855892746252171976963428465437519630424007803753141817003956

5 of 7




<a name="br6"></a>Challenge France Cybersécurité 2023 Quentin R.

print(bb.order())

\# 28948022309329048855892746252171976963428465437519630424007803753141817003956

` `Il est intéressant de constater que l’ordre de 2 · A et l’ordre de 2 · B est précisément 2fois inférieur à l’ordre de (E). Ceci signiﬁe que ces deux points sont deux générateurs de l’unique sous-groupe ⟨2 · G⟩, et cela implique également que A et B étaient des générateursde (E).

` `Finalement, il est important de noter que l’ordre de (E) est un multiple de 8, mais pasun multiple de 16. Notons alors k le huitième de l’ordre de E. k possède alors un inversemodulaire modulo 2, et il est possible de calculer cet inverse :

k = ordre // 8 h = (k + 1) // 2

\# 3618502788666131106986593281521497120428558179689953803000975469142727125495

h est l’unique nombre tel que 2 · h = 1 mod k. En eﬀet, 2 · h = 1 + k.

Trouver A et B Soit G n’importe quel générateur de (E). Vu que (E) est cyclique d’ordre

8k, on sait que A = G · x pour un unique x entre 0 et 8k.

On possède 2 · A = G · (2x). Si nous multiplions ce point par h, nous obtenons

(2 · A) · h = G · (2hx) = G · (x + kx)

Si par chance x est un multiple de 8, alors x = 8q pour un certain q. On obtient alors :

(2 · A) · h = G · (x + 8kq)

` `= (G · x) + (G · 8kq)= A + O

= A

` `On pourrait donc être tenté de générer des générateurs aléatoires de (E), d’espérer quex soit un multiple de 8 et retrouver la valeur de A de cette manière. Cependant, voici uneautre manière de procéder sans calculer plus de générateurs quand x n’est pas un multiplede 8.

Supposons que x = 8q + r pour q, r entiers et 0 ≤ r < 8. Alors,

(2 · A) · h = G · (x + k(8q + r)) = (G · x) + (G · 8kq) + (G · kr) = A + O + G · kr

(2 · A) · h − G · kr = A

` `Tester les 8 diﬀérentes valeurs de r permet de retrouver la valeur de A à coup sûr. Onpeut procéder de la même manière pour retrouver B.

6 of 7




<a name="br7"></a>Challenge France Cybersécurité 2023 Quentin R.

3 Implémentation

3\.1 Elliptic Addventure

A = aa \* h

partie = long\_to\_bytes(int(A[0])) print(partie.decode(), end = '')

B = bb \* h

partie = long\_to\_bytes(int(B[0]))print(partie.decode())

\# FCSC{a0c43dbbfaac7a84b5ce7feb81d492431a69a214d768aa4383aabfd241}

3\.2 Elliptic Addrenaline

for r in range(8):

A = aa \* h - G \* k \* rif A + A == aa:

partie = long\_to\_bytes(int(A[0]))if partie.startswith(b"FCSC{"): print(partie.decode(), end = '') break

for r in range(8):

B = bb \* h - G \* k \* rif B + B == bb:

partie = long\_to\_bytes(int(B[0]))if partie.endswith(b"}"): print(partie.decode()) break

\# FCSC{1f0b8b8d4ff304004126f245ee5f46d8961b60dff4b187ef6fe4f09e34}

7 of 7
