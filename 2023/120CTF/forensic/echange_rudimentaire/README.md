## Echange rudimentaire

Wireshark:

- Suivre le trafic TCP:
	- CTRL A -> enregistrer le flut brut dans `secrets.txt`
	- en lisant la conversation : fichier chiffré avec `openssl` en AES-CBC avec mdp=`toto`

- Déchiffrer avec openssl puis lire l image

