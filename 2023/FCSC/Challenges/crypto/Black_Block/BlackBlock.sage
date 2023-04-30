import json

FF.<a> = GF(2 ** 128)

class BlackBlock:
    def __init__(self, key):
        self._K = self.__b2FF(key)

    def __b2i(self, b):
        return int.from_bytes(b, 'big')

    def __i2FF(self, i):
        return FF.fetch_int(i)

    def __b2FF(self, b):
        return FF.fetch_int(int.from_bytes(b, 'big'))

    def __FF2b(self, k):
        return int.to_bytes(k.integer_representation(), 16, "big")

    def __xor(self, A, B):
        return bytes([ a ^^ b for a, b in zip(A, B) ])

    def E(self, B):
        K = self._K
        for _ in range(64):
            B += K
            if B != 0:
                B = (1 + a + a**3) / B**4
            K = (K + a)**3
        B += K
        return B

    def encrypt(self, plaintext):
        ciphertext = b""
        iv = os.urandom(16)
        cnt = self.__b2i(iv)
        for i in range(0, len(plaintext), 16):
            Z = self.__FF2b(self.E(self.__i2FF(cnt)))
            P = plaintext[i:i+16]
            C = self.__xor(Z, P)
            ciphertext += C
            cnt = (cnt + 1) % 2**128
        return iv, ciphertext

if __name__ == '__main__':

    k = os.urandom(16)
    E = BlackBlock(k)

    p = os.urandom(48)
    iv, c = E.encrypt(p)
    print(json.dumps({
        "iv": iv.hex(),
        "p": p.hex(),
        "c": c.hex(),
    }))

    flag = open('flag.txt', 'rb').read()
    iv, flag_enc = E.encrypt(flag)
    print(json.dumps({
        "iv": iv.hex(),
        "flag_enc": flag_enc.hex(),
    }))
