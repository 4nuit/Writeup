# Comparaison

**Category** : intro
**Points** : 20

> _Cette épreuve fait partie de la série qui utilise la machine virtuelle du FCSC 2023, plus d'informations sur celle-ci ici : https://www.france-cybersecurity-challenge.fr/vm_

Afin de se familiariser avec la machine virtuelle et son langage assembleur, vous devez écrire dans cette épreuve un code assembleur qui effectue une comparaison.

La machine est initialisée avec deux valeurs aléatoires dans les registres `R5` et `R6`.
À la fin du programme, `R0` doit contenir `1` si les valeurs sont différentes, `0` sinon.

Le code machine (_bytecode_) sera envoyé sous un format hexadécimal, qu'on pourra générer à l'aide de l'assembleur fourni (fichier `assembly.py`).

`nc challenges.france-cybersecurity-challenge.fr 2300`

## Files : 
