import oqs
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Classical RSA public key
N = 24663070886662364809205384541406416365408019755807151423141951855039480831436722243048094362521489268594863814626148670355043399290150726081687256603673615254637646573780722126152184975600867818686601225997838349092568023063065679269632110437398488483406050740033405566859734330123390412285392709312815124924903074775152743688190869304087503418491001016228321512541594176787057666816337694954832451362922803351587903654856005244214887802707452097421002978115246966225182258593836866364454158302294031773383064242261121923019463353900201239486860118081442146532621484809767279339311345030547350261879658671459984953173
e = 65537
rsa_public_key = rsa.RSAPublicNumbers(e,N).public_key(backend=default_backend())

# Post-quantum Kyber public key
Kyber_PK =  "W4BMahiqIMcdF3QAD6xUckkl35kPyylMSxTKSUKo4EgcFPw9ZRueguZT02gajLBx9GaTJ1eMzzNfb2qjH+QmUrbNlQc7hPKbGDIm+LJtvnpVJ3" + \
            "oumcRBiwWZ+weVQIdDDgGC3FVRNUSyrZC0uEmRnKeksZvPC+Opawh6vBhKXhcNpspCGvypjwwGAPUiBAOn8Wmk0nGg7cxFvyWObxgN/oxbnUPO" + \
            "KxZXWzZef1B9psG/uLgKLwsRFLp7fgIKn5M7H8ujNJsl2qSGONcAGXJ+0IaiIRFfXaJXqvBiHlg6FiO1wruCiKhrl9ign3Q2axOtdoxT6xemuo" + \
            "zFesFj3jc+1ZhnC7xbzZaxnBC1bzUJJ4alF/wKVyfE/KYE3TMd6IqQwjmrT/mKXYHMtQdJ7vM/B2U/r2R1rSVe3KJWmkQpMaZ/YEFJIcE5Ajsn" + \
            "6llDglyCAVBd7ZZpXbGqUiQ3kIC9XvkrkVwQiuRXI8BiuMlJOQRZVhtVPkqWrPGW0KpCz6JxAlFHvjOzxaafzlWgn6QlgHg1AsS+Tpsus0cp82" + \
            "Vvi/Qf0Jm/5WiDJeUzF5KVPZsIDpwObHKFy7AK8DsFORwxLvgl/jtH1vysnCSnrZA64bBzwvPCB/bL6/Sw1ZStpERWrBhOVgmeIXtWYshuXwx9" + \
            "57iJJ9EuQHyQWMeNqdbKrDODC4JEOmhFmCFcTcKI+JwBcmq4fqaeCWp84nsM9sUzGGRlosVz7jsu5Vh+RDIXe5Sq99SzHxYnEouhPOljzLSKjo" + \
            "Jd3ZtaYMUJhnorrNdnsiaZ1KZ/ajcLEsK53RloqlohOiSR1hu77AV9BwWuT/MZl1ISdHeZLzwKmpzAGXCseUPJxNKcIPafrdO+MhKKbnUcSPin" + \
            "ESOoEXRCJdSTP2IHConO9ieUUGikFXw3ugx6psm9AukI+Yddq+VjkrMlnUlZ6Fd6ZbljVjvGEZczcEbEu/J92Tc8HDNdxZCs5EdU/8Jzxexhsc" + \
            "g0EPF7qTxtclO9oRlJUaNYdWnFCXmx9pmj54kMjfEs1sXGwKGOHK+ADpguYFKtGOljyRdmQhGf2eU="

# Hybrid encapsulation
postquantum_header, shared_secret = oqs.KeyEncapsulation("Kyber512").encap_secret(base64.b64decode(Kyber_PK))
classical_header = rsa_public_key.encrypt(
    shared_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None),
    )

# Read plaintext
file_plaintext = open("message.txt", "rb")
data = file_plaintext.read()
file_plaintext.close()

# Encrypt data
encryptor = Cipher(algorithms.AES(shared_secret),modes.CTR(16*b'\x00'),backend=default_backend()).encryptor()
ciphertext = encryptor.update(data) + encryptor.finalize()

# Write ciphertext
file_ciphertext = open("encrypted.bin", "wb")
file_ciphertext.write(postquantum_header + classical_header + ciphertext)
file_ciphertext.close()