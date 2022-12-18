from string import printable
super_liste = printable
def hide(var0):
        var1 = ""
        var2 = "GORFOU"
        var3 = 0
        for i in range(len(var0)):
                try:
                        var4 = var0[i]
                        var4 = chr(ord(var4) + (ord(var2[i % len(var2)])- 100) )
                        var1 = var1 + var4
                except:
                        return ""

        return var1

flag_ciphered = "6_OTf;Da\"ATDB>\u001fO;]Hh"
flag = ""
super_liste = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!_"
for i in range(len(flag_ciphered)):
    for x in super_liste:
        flag_ciphered = "6_OTf;Da\"ATDB>\u001fO;]Hh"
        flag_actu = str("Star{"+flag+x)
        yo = hide(flag_actu)
    
        if yo[int(len(flag_actu)-1)] == flag_ciphered[int(len(flag_actu)-1)]:
            flag +=x
            print("[+] Flag: " + flag)
            break
