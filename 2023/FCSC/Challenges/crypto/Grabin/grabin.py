import os
import json
from hashlib import sha256
from fractions import Fraction
from Crypto.Cipher import AES
from Crypto.Random.random import randrange
from Crypto.Util.number import isPrime
from Crypto.Util.Padding import pad

class G:
    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im >= 0: return f"{self.re} + {self.im}*I"
        else:            return f"{self.re} - {abs(self.im)}*I"

    def __repr__(self):
        return self.__str__()

    def __add__(self, e):
        re = self.re + e.re
        im = self.im + e.im
        return G(re, im)

    def __sub__(self, e):
        re = self.re - e.re
        im = self.im - e.im
        return G(re, im)

    def __mul__(self, e):
        re = self.re * e.re - self.im * e.im
        im = self.re * e.im + self.im * e.re
        return G(re, im)

    def __mod__(self, d):
        _, r = self.__eucl(d)
        return r

    def __eucl(self, d):
        nn = d.norm()
        re = Fraction(self.re * d.re + self.im * d.im, nn)
        im = Fraction(self.im * d.re - self.re * d.im, nn)
        q = G(round(re), round(im))
        r = self - d * q
        return q, r

    def __pow__(self, e, m):
        b = G(1, 0)
        tmp = self
        while e:
            if e == 1:
                b = (b * tmp) % m
            tmp = (tmp * tmp) % m
            e = e // 2
        return b

    def norm(self):
        return self.re ** 2 + self.im ** 2

    def isGoodPrime(self):
        nn = self.norm()
        return isPrime(nn) and (self.norm() % 8 == 5)

class Grabin:
    def __init__(self, l = 256):
        re = randrange(2 ** l)
        im = randrange(2 ** l)
        p = G(re, im)
        while not p.isGoodPrime():
            p += G(randrange(2 ** 32), randrange(2 ** 32))

        q = G(re - im, re + im)
        while not q.isGoodPrime():
            q += G(randrange(2 ** 32), randrange(2 ** 32))

        self.l = l
        self.pk = p * q
        self.sk = (p, q)

    def encrypt(self, flag):
        # Random message
        re = randrange(2 ** self.l)
        im = randrange(2 ** self.l)
        m = G(re, im)

        # Encapsulation
        x = pow(m, 4, self.pk)
        m = f"({m.re},{m.im})".encode()
        k = sha256(m).digest()

        # Encrypt the flag
        iv = os.urandom(16)
        c = AES.new(k, AES.MODE_CBC, iv).encrypt(pad(flag, 16))

        # Return challenge values
        return x, iv, c

if __name__ == "__main__":

    flag = open("flag.txt", "rb").read().strip()

    C = Grabin()
    x, iv, c = C.encrypt(flag)
    print(json.dumps({
        "l":  C.l,
        "n":  str(C.pk),
        "x":  str(x),
        "iv": iv.hex(),
        "c":  c.hex(),
    }))
