from pwn import *

shell = ssh(host='bash-hell.flag4all.sh', user='the_gate', port=666, password='iop')
shell.execute('nc bashcat 666')

def repondre(question):
	shell.sendline(question)
	reponse = shell.recvuntil('Too slow.')
	return reponse

with open('list.csv', 'r') as file:
	reponses = file.readlines()

for reponse in reponses:
	print(repondre(reponse))

shell.close()
