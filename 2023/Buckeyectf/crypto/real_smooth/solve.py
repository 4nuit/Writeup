def xor_hex(xs, ys):
    #print(xs, ys)
    return "".join(hex(int(x, 16) ^ int(y,16))[2:] for x, y in zip(xs, ys))

def hexToByteArray(xs):
    retVal = b''
    newA = [int(xs[i:i+2], 16) for i in range(0, len(xs), 2)]
    for a in newA:
        retVal += a.to_bytes(1, 'big')
    return retVal


lines = open("database.txt", "rb").readlines()

emptyHex = '0824f2dc11e8510fc249ad48' #Hex that ends most strings to read thru for guessable plaintext
# Technically the first byte of this is a \n character, so I xor with a \n "0a" followed by "20" for spaces

# Print ciphertext half decoded
for line in  lines:
    lineHex = line[:18*2].decode()
    val = xor_hex(lineHex, xor_hex("20"*6+"0a"+"20"*11, emptyHex.rjust(36, "0"))) #Xors space aka "20" with known empty hex, then xors line with that
    print(hexToByteArray(val))
    # With this, you can read the plaintext and find "ousomuch\n", which can be guessed as "iloveyousomuch\n"

# Now that we know that, we can find the line with ousomuch\n and save the hex of it
hexForXOR = ""
for line in  lines:
    lineHex = line[:18*2].decode()
    val = xor_hex(lineHex, xor_hex("20"*6+"0a"+"20"*11, emptyHex.rjust(36, "0"))) #Xors space aka "20" with known empty hex, then xors line with that
    if b'ousomuch' in hexToByteArray(val):
        hexForXOR = lineHex

basePlaintext = b"iloveyousomuch\n   ".hex()

# Now we use this line as a base 
for line in lines:
    lineHex = line[:18*2].decode()
    val = xor_hex(lineHex, xor_hex(basePlaintext, hexForXOR))
    if b'}' in hexToByteArray(val):
        print(hexToByteArray(val))
    if b'{' in hexToByteArray(val):
        print(hexToByteArray(val))
