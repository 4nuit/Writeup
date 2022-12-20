https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/docker-forensics

On nous donne un nom d'image que l'on récupère:

```
sudo docker pull shisuiyogo/christmas
```

# Approche n°1:

On essaie de lancer le conteneur. Pas de chance, c'est de l'armv8 (docker inspect):

```
sudo docker run -it shisuiyogo/christmas
```

WARNING: The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64) and no specific platform was requested
exec /bin/bash: exec format error

Historique:

```
sudo docker history [--no-trunc] shisuiyogo/christmas
```

IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
81ef8c98117b   44 hours ago   RUN /bin/sh -c rm /data/secret_note.txt # bu…   0B        buildkit.dockerfile.v0
<missing>      44 hours ago   COPY secret_note.txt /data/ # buildkit          45B       buildkit.dockerfile.v0
<missing>      11 days ago    /bin/sh -c #(nop)  CMD ["bash"]                 0B        
<missing>      11 days ago    /bin/sh -c #(nop) ADD file:eb8b2914800b2ed86…   56.7MB    


```
sudo docker cp <id>:/data/secret_note.txt secret_note.txt
```

-> ne sert à rien car le conteneur efface le fichier

Find:

```
sudo find / -name "secret_note.txt" 2>/dev/null
```

![alt text](https://github.com/0x14mth3n1ght/Writeup/blob/master/Yogosha/Welcome/find.png)

Il ne reste plus qu'à afficher le premier fichier

# Approche n°2:

https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout

```
sudo docker save shisuiyogo/christmas > image.tar
mkdir image; cd image; tar -xf ../image.tar
```

On inspecte les couches jusqu'à trouver:
```
cd 83a876e6bc15edb67a6feed676fdc1929e8019067cb0dd02846e1365e8a0c925
tar -xf layer.tar
cd data; cat secret*
```

![alt text](https://github.com/0x14mth3n1ght/Writeup/blob/master/Yogosha/Welcome/image.png)
