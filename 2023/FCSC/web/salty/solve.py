import sys
import requests
import time

if len(sys.argv) < 2:
    print("Usage: python solve.py <pass>")
    sys.exit()

password = sys.argv[1]

i = 0
while True:
	response = requests.get(f'https://salty-authentication.france-cybersecurity-challenge.fr/?password={password}')
	print(response.text)
	if "Wrong" not in response.text:
 		break
	time.sleep(0.5)
	print("essai n° ", i)
	i+=1

