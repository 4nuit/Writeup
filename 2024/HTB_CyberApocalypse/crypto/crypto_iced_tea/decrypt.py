from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b

def decrypt_block(ciphertext, key):
    BLOCK_SIZE = 64
    DELTA = 0x9e3779b9
    msk = (1 << (BLOCK_SIZE // 2)) - 1

    m = b2l(ciphertext)
    m0 = m >> (BLOCK_SIZE // 2)
    m1 = m & msk

    K = [b2l(key[i:i+4]) for i in range(0, len(key), 4)]

    s = DELTA << 5
    for i in range(32):
        m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
        m1 &= msk
        m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
        m0 &= msk
        s -= DELTA

    return l2b(m0) + l2b(m1)

def decrypt_ecb(ciphertext, key):
    BLOCK_SIZE = 64
    decrypted_blocks = []
    for i in range(0, len(ciphertext), BLOCK_SIZE // 8):
        block = ciphertext[i:i + BLOCK_SIZE // 8]
        decrypted_block = decrypt_block(block, key)
        decrypted_blocks.append(decrypted_block)
    return b''.join(decrypted_blocks)

if __name__ == '__main__':
    KEY = bytes.fromhex('850c1413787c389e0b34437a6828a1b2')
    ciphertext = bytes.fromhex('b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843')

    plaintext = decrypt_ecb(ciphertext, KEY)
    print(plaintext.decode())
