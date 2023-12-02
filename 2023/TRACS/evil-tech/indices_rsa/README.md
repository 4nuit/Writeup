***** DESCRIPTION *****************************************************************************************************************************************

Nous disposons d’un fichier public_key.pem récupéré sur le serveur d’Eviltech. En remontant des logs, nous savons qu’il a été généré en utilisant les deux commandes suivantes :
openssl genrsa -out private_key.pem 2048
et
openssl rsa -RSAPublicKey_out -in private_key.pem -out public_key.pem
***************************************************************************************************************************************************************************
