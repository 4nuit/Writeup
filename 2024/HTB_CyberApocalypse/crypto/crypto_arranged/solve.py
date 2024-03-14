from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from hashlib import sha256

# Points A et B fournis
A = (6174416269259286934151093673164493189253884617479643341333149124572806980379124586263533252636111274525178176274923169261099721987218035121599399265706997,
     2456156841357590320251214761807569562271603953403894230401577941817844043774935363309919542532110972731996540328492565967313383895865130190496346350907696)
B = (4226762176873291628054959228555764767094892520498623417484902164747532571129516149589498324130156426781285021938363575037142149243496535991590582169062734,
     425803237362195796450773819823046131597391930883675502922975433050925120921590881749610863732987162129269250945941632435026800264517318677407220354869865)

# Fonction pour résoudre le logarithme discret
def solve_log_discrete(A, B):
    # On cherche à exprimer priv_a * G = A et priv_b * G = B
    # Cela signifie que G = A / priv_a = B / priv_b
    G = (A[0] * B[1] - B[0] * A[1], A[1] - B[1])  # Calcul de G en utilisant les formules ci-dessus
    
    # Maintenant que nous avons trouvé G, nous pouvons calculer priv_a et priv_b
    priv_a = B[0] * G[1] // G[0]  # priv_a = B_x / G_x
    priv_b = A[0] * G[1] // G[0]  # priv_b = A_x / G_x
    
    return priv_a, priv_b

# Résolution du logarithme discret
priv_a, priv_b = solve_log_discrete(A, B)
print("Valeur de priv_a :", priv_a)
print("Valeur de priv_b :", priv_b)


#C = priv_a * B[0]; print(C); print(priv_b * A)
secret = 0

hash = sha256()
hash.update(long_to_bytes(secret))

key = hash.digest()[:16]
ct = b'V\x1b\xc6&\x04Z\xb0c\xec\x1a\tn\xd9\xa6(\xc1\xe1\xc5I\xf5\x1c\xd3\xa7\xdd\xa0\x84j\x9bob\x9d"\xd8\xf7\x98?^\x9dA{\xde\x08\x8f\x84i\xbf\x1f\xab'[16:]
iv = b'V\x1b\xc6&\x04Z\xb0c\xec\x1a\tn\xd9\xa6(\xc1\xe1\xc5I\xf5\x1c\xd3\xa7\xdd\xa0\x84j\x9bob\x9d"\xd8\xf7\x98?^\x9dA{\xde\x08\x8f\x84i\xbf\x1f\xab'[:16]
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(pad(ct, 16))
print(f'plaintext = {decrypted}')
