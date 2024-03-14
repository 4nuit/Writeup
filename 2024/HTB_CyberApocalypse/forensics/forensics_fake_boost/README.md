## Part 1

Wireshark-> exporter objets HTTPs.

On remarque du Powershell obfusqué. Le code décodé est dans `fake.pwsh`.
On remarque tout en haut:

```bash
echo SFRCe2ZyMzNfTjE3cjBHM25fM3hwMDUzZCFf | base64 -d
HTB{fr33_N17r0G3n_3xp053d!_
```

## Part2

Le script va récupérer email,id,token,name puis chiffrer en AES-CBC avec la clé donnée, et l'iv est présent dans un objet http avec le ciphertext.

```bash
python solve.py 
b'[\r\n    {\r\n        "ID":  "1212103240066535494",\r\n        "Email":  "YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9",\r\n        "GlobalName":  "phreaks_admin",\r\n        "Token":  "MoIxtjEwMz20M5ArNjUzNTQ5NA.Gw3-GW.bGyEkOVlZCsfQ8-6FQnxc9sMa15h7UP3cCOFNk"\r\n    },\r\n    {\r\n        "ID":  "1212103240066535494",\r\n        "Email":  "YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9",\r\n        "GlobalName":  "phreaks_admin",\r\n        "Token":  "MoIxtjEwMz20M5ArNjUzNTQ5NA.Gw3-GW.bGyEkOVlZCsfQ8-6FQnxc9sMa15h7UP3cCOFNk"\r\n    }\r\n]\x05\x05\x05\x05\x05o15\xdbI0\xe9\xdaEpX\xbc\xf5\xd2\xb2\x8b'
```

```bash
echo YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9 | base64 -d
b3W4r3_0f_T00_g00d_2_b3_7ru3_0ff3r5}
```
