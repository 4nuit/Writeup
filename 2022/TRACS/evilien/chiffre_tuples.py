#!/usr/bin/python3

import random
import sys
rnd = random.SystemRandom()
from Crypto.Cipher import AES

filename = sys.argv[1]


def genkey():
    state = rnd.getrandbits(31)
    ret = []
    for i in range(16):
        ret += [ (state >> 16) % 256 ]
        state = ((state * 214013) + 2531011) & 0x7fffffff
    return bytes(ret)


N = 106652624346254417188496477828277711201985180386496691443452277800693108861290639747761164943196761897834240929260748033091383148829527121039874223299595937390303061397984276532090581072405086349495624932572385194341436736224927349674948373465963452183316827635350613809106526764354910385182102667468450496349


def ciphered_tuple(id,serial,memory,version,ip,password):
    plain = bytes(f'evil_crypto_header;{id};{serial};{memory};{version};{ip};{password}', encoding='utf8')
    while (len(plain) % 16) != 0:
        plain = plain + b';'
    key = genkey()
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.encrypt(plain)
    k = int.from_bytes(key,byteorder='big')
    ciphered_key = pow(k, 65537, N)
    return ciphered_key, data


with open(filename, "r") as f:
    lines = [ x for x in f.read().split('\n') if x]


for line in lines[1:]:
    id, serial, memory, version, ip, password = line.split(',')
    ciphered_key, data = ciphered_tuple(id,serial,memory,version,ip,password)
    print("%x"%ciphered_key, data.hex(),sep=';')

