# Fibonacci

**Category** : hardware
**Points** : 189

> _Cette épreuve fait partie de la série qui utilise la machine virtuelle du FCSC 2023, plus d'informations sur celle-ci ici : https://www.france-cybersecurity-challenge.fr/vm_

Cette fois, on vous demande de coder en assembleur la suite de Fibonacci.

La machine est initialisée avec une valeur `n` aléatoire (mise dans le registre `R5`) et devra contenir (dans `R0`) l'élément `Fib(n)` une fois le code exécuté.
Pour rappel :
* `Fib(0) = 0`,
* `Fib(1) = 1`,
* `Fib(n) = Fib(n - 1) + Fib(n - 2)`.

Le code machine (_bytecode_) sera envoyé sous un format hexadécimal, qu'on pourra générer à l'aide de l'assembleur fourni (fichier `assembly.py`).

`nc challenges.france-cybersecurity-challenge.fr 2301`


## Files : 
 - [challenge.py](./challenge.py)
