import os
from hashlib import sha512
from fastecdsa.curve import P521

def H(m):
    ctx = sha512()
    ctx.update(m)
    return ctx.digest()

class Random:
    def __init__(self):
        self.state = int.from_bytes(os.urandom(16), "little")
        self.a = 200565257846616591441313188858237974233
        self.c = 1
        self.m = 128

    def randint(self):
        r = self.state
        self.state = (self.a * self.state + self.c) % 2 ** self.m
        return r

    def nonce(self):
        r = 0
        r = (r << self.m) | self.randint()
        r = (r << self.m) | self.randint()
        r = (r << self.m) | self.randint()
        r = (r << self.m) | self.randint()
        return r

class ECDSA:
    def __init__(self):
        self.C = P521
        self.rng = Random()
        self.sk = int.from_bytes(os.urandom(48), "little")
        self.Q = self.sk * self.C.G
        assert self.Q.IDENTITY_ELEMENT != self.Q

    def sign(self, msg):
        k = self.rng.nonce()
        h = int.from_bytes(H(msg), "little")
        P = k * self.C.G
        r = P.x % self.C.q
        assert r > 0, "Error: cannot sign this message."

        s = (pow(k, -1, self.C.q) * (h + self.sk * r)) % self.C.q
        assert s > 0, "Error: cannot sign this message."

        return r, s

    def verify(self, msg, sig):
        r, s = sig
        if r < 1 or r >= self.C.q: return False
        if s < 1 or s >= self.C.q: return False
        h = int.from_bytes(H(msg), "little")
        s_inv = pow(s, -1, self.C.q)
        u = h * s_inv % self.C.q
        v = r * s_inv % self.C.q
        P = u * self.C.G + v * self.Q
        return r == P.x

if __name__ == "__main__":

    try:
        S = ECDSA()
        print(f"Public Point Q: ({S.Q.x}, {S.Q.y})")
        print("Here is a valid signature!")
        m = os.urandom(24)
        r, s = S.sign(m)
        print(f"m = 0x{m.hex()}")
        print(f"sig = ({r}, {s})")
        assert S.verify(m, (r, s))

        print("You turn! Give me another one!")
        r = int(input("r = "))
        s = int(input("s = "))
        sig = (r, s)
        if S.verify(b"All right, everybody be cool, this is a robbery! Give me the flag!", sig):
            flag = open("flag.txt").read()
            print(flag)
        else:
            print("Nope!")
    except:
        print("Please check your inputs.")
