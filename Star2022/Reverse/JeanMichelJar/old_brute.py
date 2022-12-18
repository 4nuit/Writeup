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

def brute():
        s="6_OTf;Da\"ATDB>\u001fO;]Hh"
        flag="Star{"
        for i in range(5,len(s)):
                a=0
                while (a==0):
                        for j in super_liste:
                                if (hide(flag+j)==s[:i]):
                                        flag+=j
                                        print("flag=",flag)
                                        a=1

        return flag

print(brute())
