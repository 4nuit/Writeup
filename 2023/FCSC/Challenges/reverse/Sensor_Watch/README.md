# Sensor Watch

**Category** : reverse
**Points** : 454

Vous remarquez qu'un de vos collègues triture sa montre CASIO F-91W avant de rentrer le mot de passe de son ordinateur.
Après l'avoir interrogé à ce sujet, il vous remet sa montre et une clé USB contenant un seul dossier `emulateur` et vous met au défi de retrouver son mot de passe.

Vous désossez la montre et ô surprise, le PCB ne semble pas d'origine...
Vous dumpez le contenu de la flash dans le fichier `watch.uf2`.

Vous jouez un peu avec l'émulateur et vous tombez sur une interface qui vous demande un code PIN...
Vous essayez la date de naissance de votre collègue, mais la montre affiche `BADPIN`.

**Attention :** pour cette épreuve, vous n'avez que 10 tentatives de flag. Le flag correspond à ce qui est affiché par la montre quand vous trouvez le bon code PIN.

* SHA256(`watch.uf2`) = `f30e57fd42111d244b86387832694cbc242da5820cfd0a66bb9806642eda28ea`
* SHA256(`emulateur.tar.gz`) = `12f8a657a17ae7e8bc96b5be155f3d9e1281d47cce8ed808a276c648f991e879`


## Files : 
 - [emulateur.tar.gz](./emulateur.tar.gz)
 - [watch.uf2](./watch.uf2)


