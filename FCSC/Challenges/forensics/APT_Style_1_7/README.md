# APT Style 1/7

**Category** : forensics
**Points** : 389

##### Description générale pour la série

En tant que RSSI, vous anticipez ~ tardivement ~ la migration des postes utilisateur de votre parc vers Windows 10.

Pour ce faire, vous demandez à l'un de vos collaborateurs de préparer un ISO d'installation et, devant l'importance de l'innocuité de ce média d'installation, vous décidez de le tester.
Vous observez d'étranges comportements sur la machine fraîchement installée...
Vous décidez alors de décortiquer cet ISO, afin de comprendre d'où viennent ces comportements.

**Ce challenge est en 7 parties, selon le découpage initial suivant** :
- `APT Style 1/7` :
    * 500 points de départ
- `APT Style 2/7` :
    * 500 points de départ,
    * débloqué après `APT Style 1/7`
- `APT Style 3/7` :
    * 100 points de départ,
    * débloqué après `APT Style 2/7`
- `APT Style 4/7` :
    * 100 points de départ,
    * débloqué après `APT Style 2/7`
- `APT Style 5/7` :
    * 100 points de départ,
    * débloqué après `APT Style 2/7`
- `APT Style 6/7` :
    * 100 points de départ,
    * débloqué après `APT Style 2/7`
- `APT Style 7/7` :
    * 200 points de départ,
    * débloqué après `APT Style 2/7`

**Attention** : pour ces épreuves, vous n'avez que 10 tentatives de flag par épreuve.

Toutes les épreuves de cette série utilisent le **même fichier** disponible ci-dessous.

SHA256(`Win10_22H2_French_x64.iso`) = `6b308977cecc9b6d8aa50a8ddabdacdf01394b0819d5978141ed61862c61143f`.

--- 

##### Question 

Quel objet déclenche le comportement malveillant ?
La réponse attendue est le **chemin** de l'objet.

Quel groupe d'attaquants emploie une méthode similaire ?
Le format attendu est `UNCXXXX`.

Le flag final est au format `FCSC{<chemin>:UNCXXXX}`


## Files : 
