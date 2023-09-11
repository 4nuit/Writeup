he = open("he.txt","rb").read()
she= open("she.txt","rb").read()

res = ""
i=0
j=0
count=0
window = 3
diff=[]
try:
  while count<100 :
    while he[i]==she[j]:
        i+=1
        j+=1
    print("diff at ",i,j)
    print(he[i],she[j], he[i-window:i+window])
    print(he[i+1],she[j+1],she[j-window:j+window])
    if he[i]==she[j+1] and he[i+1]==she[j+2]:
        diff.append(("",she[j]))
        res+=chr(she[j])
        j+=1
        print(">>")

    elif he[i+1]==she[j] and he[i+2]==she[j+1]:
        diff.append((he[i],""))
        res+=chr(he[i])
        i+=1
        print("<<")

    else:
        diff.append((he[i],she[j]))
        res+="("+chr(he[i])+"|"+chr(she[j])+")"
        i+=1
        j+=1
        print("==")
    count+=1
    
except: 
    pass

print(res)
