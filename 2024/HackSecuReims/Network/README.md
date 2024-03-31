## Anomaly Adventure

Avec Wireshark, on remarque un header JFIF dans les paquets TCP.
On extrait donc l'image en cli:

```bash
tshark -2 -r capture.pcap -T fields -e data > extracted
xxd -r -p extracted > extracted.jpg
file extracted.jpg 
extracted.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=5, xresolution=74, yresolution=82, resolutionunit=1], progressive, precision 8, 1200x800, components 3
```

```bash
exiftool extracted.jpg
echo SFNSe1NvbWVib2R5X29uY2VfdG9sZF9tZX0= | base64 -d
```

Flag:
`HSR{Somebody_once_told_me}`

## POP3

```bash
git clone https://github.com/openwall/john
cd john/run
./apop2john.py ../../capture.pcap > ../../hash.txt
cd ../..
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (dynamic_1017 [md5($s.$p) (long salt) 128/128 AVX 4x3])
No password hashes left to crack (see FAQ)
```

Flag:
`HSR{LAUPALANGIHE4}`

## ICMP

Comme Anomaly Adventure, en CLI, on remarque après extraction un format YENC:

```bash
tshark -2 -r capture.pcap -T fields -e data > extracted
xxd -r -p extracted > extracted.txt 
```

Au milieu des encodages YENC (non-alphanumériques), on repère de la base64 cachée dans les trames envoyées:

```
echo U0ZOU2UwaHZkWE4wYjI1ZmQyVmZhR0YyWlY5aFgzQnliMkpzWlcwaGZRP | base64 -d | base64 -d
```

Flag:
`HSR{Houston_we_have_a_problem!}`
