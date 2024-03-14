from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64decode

ct = open("rj1893rj1joijdkajwda","rb").read()
ct = b64decode(ct)
iv = ct[:16]
ct = ct[16:]

key = b64decode("Y1dwaHJOVGs5d2dXWjkzdDE5amF5cW5sYUR1SWVGS2k=")

cipher = AES.new(key,AES.MODE_CBC,iv)
decrypted = cipher.decrypt(pad(ct,16))
print(decrypted)
