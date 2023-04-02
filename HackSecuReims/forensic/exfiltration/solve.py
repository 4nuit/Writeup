import pandas as pd
flag=""
df = pd.read_csv("exfil.csv")
pktimes = list(df["Info"])
for el in pktimes:
	if "flag" in el:
		flag+='0'
	else:
		flag+='1'
print(flag)
"""
pktimes.pop(0)
print("".join(map(str,pktimes)))
"""

"""
Il fallait regarder la version de HTTP (0 ou 1) au lieu des requêtes à /bin ou /flag
"""
