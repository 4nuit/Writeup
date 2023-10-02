import pwn

hex = "1:10:D0:10:42:41:34:20:B5:40:03:30:91:C5:E1:E3:D2:A2:72:D1:61:D0:10:E3:A0:43:C1:01:10:B1:B1:B0:B1:40:9".replace(":", "")
hex_sequence = bytes.fromhex(hex)
print(pwn.xor(hex_sequence,"snub_wrestle"))
