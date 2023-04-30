from Crypto.Util.number import bytes_to_long

flag = open("flag.txt", "rb").read().strip()
assert len(flag) == 64

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = -3
b = 41058363725152142129326129780047268409114441015993725554835256314039467401291

K = GF(p)
E = EllipticCurve([K(a), K(b)])

mid = len(flag) // 2
Ax = K(bytes_to_long(flag[:mid]))
Bx = K(bytes_to_long(flag[mid:]))

A = E.lift_x(Ax)
B = E.lift_x(Bx)

print(f"{A + B = }")
print(f"{A - B = }")
