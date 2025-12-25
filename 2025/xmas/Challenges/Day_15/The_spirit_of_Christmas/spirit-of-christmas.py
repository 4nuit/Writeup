import os
from Crypto.Cipher import AES

try:
    with open("./flag.txt", "rb") as f:
        flag = f.read()
except FileNotFoundError:
    flag = b'RM{this_is_a_fake_flag_its_not_the_real_flag!!!}'

class LFSR(object):
    def __init__(self, seed):
        self._s = [(seed >> i) & 1 for i in range(128)]
        self._t = [0, 13, 18, 28, 37, 42, 59, 65, 71, 83, 84, 103, 107, 108, 114, 121, 127]
        for _ in range(256):
            self.bit()

    def _sum(self, L):
        s = 0
        for x in L:
            s ^= x
        return s

    def _clock(self):
        b = self._s[0]
        self._s = self._s[1:] + [self._sum(self._s[p] for p in self._t)]
        return b

    def bit(self):
        return self._clock()

    def byte(self):
        c = 0
        for i in range(8):
            c <<= 1
            c += self.bit()
        return c

key = os.urandom(16)

cipher = AES.new(key, AES.MODE_ECB)

seed = os.urandom(16)

lfsr = LFSR(int.from_bytes(seed, "big"))

print("In the ✨ spirit of Christmas ✨, I allow you to encrypt whatever you want")

msg = bytes.fromhex(input("> "))
assert len(msg) % 16 == 0

ct = cipher.encrypt(msg)

print("But I'm still a little mean")

print(bytes([c ^ lfsr.byte() for c in ct]).hex())

print(AES.new(seed, AES.MODE_ECB).encrypt(flag).hex())
