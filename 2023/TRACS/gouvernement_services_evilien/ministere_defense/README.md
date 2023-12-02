
***** DESCRIPTION *****************************************************************************************************************************************

Le nom de l’Amiral BOL revient régulièrement dans cette histoire. Nous pourrions regarder du côté du site du Ministère de la Défense évilien (https://mindef_{{votre code d’équipe}}.tracs.viarezo.fr) si des vulnérabilités existent…

Attention : Le site tourne sur une VM qui vous est attribuée. Le brute force y est autorisé (pas forcément nécessaire cependant) mais si vous y allez trop fort, seule votre équipe sera pénalisée !
Redémarrage des VMs tombées chaque heure.
***************************************************************************************************************************************************************************

https://mindef_{{id_equipe}}.tracs.viarezo.fr

## Solution

### Partie1 - Nom du proprietaire du zip

On énumère

`ffuf -c -w `fzf-wordlists` -u "http://mindef_{{id_equipe}}.tracs.viarezo.fr/FUZZ"`

On trouve rapidement dans le serveur Apache:
 
 - `robots.txt` indiquant un `disallow` sur 5uP3r_53cR3t_D1r3cT0rY contenant un dictionnaire

 - `files` contenant le zip

```bash
zip2john message.zip > hash
john hash --wordlist=passfindex.txt
```

On trouve `message.pdf` et le propriétaire

### Partie2 - Trouver le matricule de Matt
