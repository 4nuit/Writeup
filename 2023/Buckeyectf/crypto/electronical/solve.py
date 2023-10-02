import requests

url = lambda x: f'https://electronical.chall.pwnoh.io/encrypt?message={x}'

import string
chars = string.printable

#
#
# aaaa aaab ctf
# aaaa aabc tf{
#

def generate(prefix):
    return [prefix + c for c in chars]

from urllib import parse
def get_enc(x):
    print([x[i:i+16] for i in range(0, len(x), 16)])
    return requests.get(url(parse.quote(x))).text

known = 'a' * 16

for block_idx in range(5):
    for i in range(16):
        strings = generate(known[-15:])
        res = get_enc(''.join(strings) + 'a' * (15-i))
        blocks = [res[i:i+32] for i in range(0, len(res), 32)]
        print(blocks[0:len(strings)])
        print(blocks[len(chars)+block_idx])
        idx = [i for i in range(len(chars)) if blocks[i] == blocks[len(chars) + block_idx]][0]
        known += chars[idx]
        print(known)

print(known)
