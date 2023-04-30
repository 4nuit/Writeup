# Sous marin

**Category** : hardware
**Points** : 487

<div class="text-center">
<img class="p-3" src="/files/1ed4eb60c5f9421892a30c4f906fd899/sous-marin.svg" alt="U-Boot logo, Creative Common CC-BY-SA, original work by Heinrich Schuchardt">
</div>

Vous êtes invité par un collègue à venir tester son nouveau modèle miniature de
sous-marin. Ce modèle est équipé d'une caméra « vue à la première personne » et
d'un système adéquat pour diffuser ce flux vidéo.

Pour vous appâter, votre collègue précise que sa carte embarquée est basée sur
**un cœur Risc-V**. Vous acceptez donc immédiatement. Le soir venu, vous passez
plusieurs minutes à explorer les fonds marins du bassin du campus.
Néanmoins, au bout d'une demi-heure, le système de supervision panique et vous
perdez la communication. Vous vous jetez dans le bassin pour récupérer
le modèle. Votre collègue voit au loin des étudiants partir en courant avec du
matériel radio en main. Mais que s'est-il passé ? Est-ce que ces étudiants
auraient compromis le système du sous-marin à distance ? Vous proposez d'aider
votre collègue à extraire le contenu de sa mémoire Flash et à l'analyser.

Le lendemain, après une douche et une courte nuit de repos, votre collègue
dépose la carte électronique du sous-marin sur votre bureau.
Il vous confirme qu'il a implémenté
[un port série en mode 8-N-1](https://en.wikipedia.org/wiki/8-N-1), mais il
précise qu'il a potentiellement fait **une erreur d'implémentation dans la
logique du port série synthétisé**, mais il ne s'en souvient plus trop.

Parce que le sous-marin n'est pas sous l'eau, son électronique n'est pas
correctement refroidie. Vous ne pouvez pas le garder allumé plus que quelques
minutes avant qu'il ne s'éteigne par sécurité.

Vous prenez un adaptateur port série vers USB pour vous connecter sur le système
et vous commencez à investiguer...

**Pour s'interfacer avec le port série à distance, vous aurez besoin de Telnet.**

`HOST:PORT` : `challenges.france-cybersecurity-challenge.fr:2303`

Votre collègue a réussi à retrouver une sauvegarde du chargeur de démarrage
`bootloader.bin` et vous indique que vous pouvez émuler la séquence de démarrage
avec la commande `qemu-system-riscv64 -M sifive_u -m 45M -kernel bootloader.bin`
(port série disponible dans `View > Serial 0`). Cela vous permet de prototyper
des idées avant de risquer d'abîmer le sous-marin.

SHA256(`bootloader.bin`) = `e06c7b272736c0d34617e9f62fd4e4c1a8d56d6df6e4f1ee83492999c4a65e6c`.

## Files : 
 - [bootloader.bin](./bootloader.bin)


