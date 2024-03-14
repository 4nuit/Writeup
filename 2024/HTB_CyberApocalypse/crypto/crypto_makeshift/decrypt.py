
FLAG = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"
flag = FLAG[::-1]
new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+1]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)
