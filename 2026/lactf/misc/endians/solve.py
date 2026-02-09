

flag = open("chall.txt","rb").read().decode('utf-8').encode('utf-32-be').decode('utf-16-le')
print(flag)
