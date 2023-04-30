from Crypto.Util.number import bytes_to_long

flag = open("flag.txt", "rb").read().strip()
assert len(flag) == 64

p = 2**255 - 19
a = 19298681539552699237261830834781317975544997444273427339909597334573241639236
b = 55751746669818908907645289078257140818241103727901012315294400837956729358436

K = GF(p)
E = EllipticCurve([K(a), K(b)])

mid = len(flag) // 2
Ax = K(bytes_to_long(flag[:mid]))
Bx = K(bytes_to_long(flag[mid:]))

A = E.lift_x(Ax)
B = E.lift_x(Bx)

print(f"{A + B = }")
print(f"{A - B = }")
