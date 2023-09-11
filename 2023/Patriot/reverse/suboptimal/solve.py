def c2(arg2):
    temp = arg2 + 0x41
    intermediate = ((temp * 0x4325c53f) >> 0x20) >> 5
    intermediate -= (temp >> 0x1f)
    var_c_5 = temp - (intermediate * 0x7a)
    if var_c_5 <= 0x40:
        var_c_5 += 0x3d
    return var_c_5


def c4(c):
    tmp = c2(c)
    return c2(tmp)

corr={}

for c in range(0x40,0x7e):
    t = c4(c)
    print(c,chr(c),t,chr(t))
    corr[chr(t)]=chr(c)
    
target = "xk|nF{quxzwkgzgwx|quitH"

res = ""
for c in target:
    print(c, corr[c])
    res+=corr[c]
    
print(res)
