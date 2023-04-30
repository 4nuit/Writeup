# keypadbol

**Category** : hardware
**Points** : 415

Lors d'une mission de tests d'intrusion physique sur un site sécurisé, votre client vous demande d'évaluer entre autres un premier accès au site utilisant un _keypad_ et demandant un mot de passe.
Seuls 10 essais sont autorisés sinon l'alarme se déclenche.

Vous avez bien sûr pensé à filmer le mot de passe lorsque le vigile le tape, malheureusement il prend ses précautions pour cacher sa main lorsqu'il le tape.

Un accès physique rapide entre deux rondes du vigile vous permet de voir que le keypad est de type "Membrane Keypad" (https://lastminuteengineers.com/arduino-keypad-tutorial/).
L'accès à la _board_ qui le pilote étant trop complexe, et n'ayant pas beaucoup de temps, vous décidez d'implanter votre analyseur logique miniature dans un petit espace discret, en le reliant aux fils de la nappe du _keypad_.
Malheureusement, sans accès à la board difficile d'avoir le _pinout_ exact mais vous ferez avec !

Vous récupérez la capture sous forme d'un fichier enregistré `capture.vcd` entre les deux rondes suivantes, une fois que le vigile a tapé son mot de passe.
Par ailleurs, du _social_ _engineering_ sur le vigile vous permet de savoir qu'il est né en 1980, sa fille en 2018, et qu'il a un chien qui s'appelle "Baba".
Armé de ces informations, vous êtes persuadé de pouvoir "cracker" le mot de passe !

**Attention :**
* La chaîne à trouver ne suit pas le format habituel. Une fois que vous l'aurez trouvée (par exemple : `abcd`), ajoutez `FCSC{}` autour pour obtenir le flag (par exemple : `FCSC{abcd}`).
* Pour cette épreuve, vous n'avez le droit qu'à **10 tentatives de flag**. Le flag est insensible à la casse.

SHA256(`capture.vcd`) = `767a7ceb3cf70af25fa17104356216196280274d97ae49d8883ded949f39b809`.

## Files : 
 - [capture.vcd](./capture.vcd)


