from jwcrypto import jwk
import os

class Config:
    DEBUG = False
    FLAG = "HTB{f4k3_fl4g_f0r_t35t1ng}"
    JWT_SECRET_KEY = jwk.JWK.generate(kty='RSA', size=2048)