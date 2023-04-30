import gmpy2
from Crypto.Util.number import getPrime, GCD

SQRT2Constant = 0xb504f333f9de6484597d89b3754abe9f1d6f60ba893ba84ced17ac85833399154afc83043ab8a2c3a8b1fe6fdc83db390f74a85e439c7b4a780487363dfa2768d2202e8742af1f4e53059c6011bc337bcab1bc911688458a460abc722f7c4e33c6d5a8a38bb7e9dccb2a634331f3c84df52f120f836e582eeaa4a0899040ca4a81394ab6d8fd0efdf4d3a02cebc93e0c4264dabcd528b651b8cf341b6f8236c70104dc01fe32352f332a5e9f7bda1ebff6a1be3fca221307dea06241f7aa81c2c1fcbddea2f7dc3318838a2eaff5f3b2d24f4a763facb882fdfe170fd3b1f780f9acce41797f2805c246785e929570235fcf8f7bca3ea33b4d7c60a5e633e3e1485f3b494d82bc6085ac27da43e4927adb8fc16e69481b04ef744894c1ea75568775190fba44fa353f48185f107dbb4a77dac64cc266eb850ed4822e1e899d034211eb71c181ec80dd4ed1a3b3423cb62e6acb96e07f9aa061a094a16b203080f7b7e36f488a515a79246344e3005da0545ab5820feaef3706e86336a418ff3fffababf23884c066deae134242ed2f48d9f17902db9392dcb8eb050fc44784505370806676e1672decc57738f21713469bd3039791011a309ffe11229a1cf54bd4ccdb64f1e738fca6b04956709055c72a8706aa88b44318bbc67b01a86817f42f94f645f2e395c03d7abb8dc12d985073c1bb548e046353f87c7991d9b140e9

def RSAKeyGen(e, size):
    p = 1
    q = 1
    t = SQRT2Constant >> ( 4096 - (size // 2) )
    while True:
        while p < t and GCD(e, p - 1) != 1:
            p = getPrime(size // 2)
        
        while q < t and GCD(e, q - 1) != 1:
            q = getPrime(size // 2)
        
        if abs(p - q) >= 2 ** 100:
            break
        
    n = p * q
    dp = gmpy2.powmod(e, -1, p - 1)
    dq = gmpy2.powmod(e, -1, q - 1)
    iq = gmpy2.powmod(q, -1, p)
    l = GCD(p - 1, q - 1)
    d = gmpy2.powmod(e, -1, ((p - 1) * (q - 1)) // l)
    return n, p, q, iq, dp, dq, d
