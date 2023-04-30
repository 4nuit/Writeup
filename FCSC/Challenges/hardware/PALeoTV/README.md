# PALeoTV

**Category** : hardware
**Points** : 467

Afin de dissimuler ses communications, un malfrat a décidé d'utiliser une diffusion par ondes radio de vidéos de type PAL particulière pour discuter avec ses acolytes.
Il espère qu'à l'aire des diffusions numériques, il restera discret.

Vous avez intercepté grâce à votre SDR une communication sensible, mais n'avez pas vraiment le matériel pour décoder le signal PAL !
Vous savez néanmoins que le malfrat utilise un récepteur PAL avec une TV **noir et blanc** (donc sans luminance ni chrominance supplémentaire) de résolution de **768 pixels par ligne et du 576i** (classique pour du PAL), et que le signal ne contient que de la vidéo (pas d'audio).

Vous avez réussi à numériser dans `capture.vcd` les signaux analogiques en isolant le signal de synchronisation ainsi que le signal de données utiles.
Vous êtes confiant dans la possibilité de décoder ce signal PAL pour trouver le message secret !

SHA256(`capture.vcd`) = `e4b198e8ff6f38a32c469ede8503f55df0c254f60696cc0094f4d70bfd819378`.


## Files : 
