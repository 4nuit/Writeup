# Mauvaise baleine

**Category** : misc
**Points** : 500

Cette année, l'équipe technique du FCSC expérimente une nouvelle méthode pour
stocker les flags dans les challenges Docker, afin de pouvoir les changer
rapidement.

Les challenges sont construits sur des images Docker "de base", qui
contiennent : le flag, un secret et un script `change_flag` qui permet
de changer le flag si vous connaissez le secret.

Nous avons développé un petit service qui permet de changer le flag dans les
images de challenges, en exécutant les images, puis en commitant les
containers avec le nouveau flag.

Malheureusement, le service s'est retrouvé exposé sur internet par erreur à
cause d'une mauvaise configuration de firewall :

`nc challenges.france-cybersecurity-challenge.fr 2053`

Pour lancer en local :
```sh
$ ./start.sh
$ nc localhost 2053
Entrer "help" pour le message d'aide

> change_flag V3ryS3cr3t FCSC{NewFlag}
flag: FCSC{ThisIsTheFl4g}
> change_flag V3ryS3cr3t FCSC{NewNewFlag}
flag: FCSC{NewFlag}
> exit
> À la prochaine !
```

**Note :**
* Vous serez déconnecté automatiquement au bout de **2 minutes**.
* Le challenge a été testé et est à résoudre sur une machine Ubuntu 22.04 (Desktop ou Server) en configuration par défaut, avec la dernière version de Docker (23.0.4), également dans sa configuration par défaut.
* Code Go : Le commentaire "_Commit the container to the original image, so that the flag is updated and available to others that want to retrieve it._" est une erreur, il serait à remplacer par : "_Commit the container to the image tagged for this session so that the flag is available in the next `change_flag` commands._"

SHA256(`mauvaise-baleine.tar.gz`) = `ad8334d07e88bce5d5290f6631266f14e09e823cf6f1d138adb4e6c002dac64c`.

## Files : 
 - [mauvaise-baleine.tar.gz](./mauvaise-baleine.tar.gz)


