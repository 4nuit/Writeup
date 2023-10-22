# Auteur

`MyThopa (ESDAcademy - ENI Nantes - HESD05)`

## Enonce

Vous avez intercepté une conversation téléphonique entre deux terroristes. Leur organisation cible les endroits qui rassemblent beaucoup de personnes. Nous pensons qu'ils préparent une prochaine attaque bientôt, aidez-nous à trouver la ville où se produira la prochaine attaque.

Le flag à trouver est la concaténation du nom de l'appelant, de son numéro de téléphone et de la ville cible. (Si espace dans nom ou ville alors remplacer par tiret « - ». case sensitive)

`ESD{John-Doe_59426587_Le-Pellerin}` 

## Doc

- https://sip.goffinet.org/wireshark/analyse-voip-wireshark/

- https://support.yeastar.com/hc/en-us/articles/360007606533-How-to-Analyze-SIP-Calls-in-Wireshark

## Sol

`Wireshark-Sip` 

nom = `Big-J`
tel = `8005000`
ville = flux rtp -> On entend la ville du *Hellfest*: `Clisson`



