from pwn import *

conn = remote('challenges.france-cybersecurity-challenge.fr', 2052)

# Récupérer la longueur du tableau
conn.recvuntil('>>> ')
conn.sendline('longueur')
longueur = int(conn.recvline().decode().strip())

# Boucle pour trier le tableau
for i in range(longueur):
    # Chercher le minimum dans la partie non triée du tableau
    min_idx = i
    for j in range(i+1, longueur):
        conn.recvuntil('>>> ')
        # Comparer l'élément j avec le minimum
        conn.sendline(f'comparer {j} {min_idx}')
        res = int(conn.recvline().decode().strip())
        if res == 0:
            min_idx = j
    
    # Échanger l'élément i avec le minimum trouvé
    if i != min_idx:
        conn.recvuntil('>>> ')
        conn.sendline(f'echanger {i} {min_idx}')
        conn.recvuntil('>>> ')

# Vérifier si le tableau est trié
conn.recvuntil('>>> ')
conn.sendline('verifier')
flag = conn.recvline().decode().strip()
print(flag)
