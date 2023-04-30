# pwnduino

**Category** : pwn
**Points** : 451

Dans le cadre d'un contrôle d'accès à un système industriel, une board AVR avec un firmware dédié implémente des
calculs sur un secret stocké ne devant pas quitter la mémoire interne du microcontrôleur. Pour déclencher
ces calculs, il est nécessaire de fournir un mot de passe d'authentification. La console se déconnecte au bout
de 10 secondes sans activité.

Lors d'une mission d'audit, on vous demande d'évaluer la sécurité de ce système, et notamment valider que
le secret très sensible ne fuite pas. Vous avez réussi à accéder à un serveur de développement sur lequel
un binaire de firmware de debug et ses fichiers source sont accessibles. Armé de ces informations, vous pensez
pouvoir récupérer ce secret sur le firmware de production !

`nc challenges.france-cybersecurity-challenge.fr 2104`

* SHA256(`firmware_debug.bin`) = `8bcd3e1c8ac6537e8b3a615fb323be8497f7e431342a60c97f1849eb5e8ea197`.
* SHA256(`src_debug.tar.gz`) = `70fcd1e3eab1259fc9a059013019b66e9b6376d8410ea4574bd84b66710e1bb2`.

**Note :** Cette épreuve comporte une erreur dans la logique du code C. Vu que celle-ci n'impacte pas du tout la résolution, les fichiers sont inchangés. Le diff suivant permettrait de corriger l'erreur :
```diff
- crc ^= pgm_read_byte(s[i]);
+ crc ^= pgm_read_byte(&(s[i]));
```

## Files : 
 - [firmware_debug.bin](./firmware_debug.bin)
 - [src_debug.tar.gz](./src_debug.tar.gz)


