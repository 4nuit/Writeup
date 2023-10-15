def decode(flag):
  if flag[0:6] != 'TCP1P{':
    oops()
  if flag[-1] != '}':
    oops()
  if flag[6:10] == 'byte':
    yeayy()
  if flag[10] and flag[15] and flag[18] != chr(95):
    oops()
  if flag[11:15] != 'code':
    oops()
  if flag[11] == flag[19]:
    yeayy()
  if flag[12] == ord(flag[20]) - 6:
    yeayy()
  if ord(flag[16]) != 105 or ord(flag[17]) != 115:
    oops()
  if flag[19] != 'H':
    oops()
  if ord(flag[20]) == 117:
    yeayy()
  if ord(flag[21]) - ord(flag[2]) != 10:
    oops()
  if flag[22].lower() == flag[0]:
    yeayy()
  if flag[22] == flag[23]:
    yeayy()
  return None

print(decode(flag))
