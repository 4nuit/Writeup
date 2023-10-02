from z3 import *

with open(r"flag_checker",'rb') as f:
    ops = list(f.read())
pc = 0
regs = [0]*0x40
t = -1

s = Solver()
flag = [BitVec(f"flag[{i}]",8) for i in range(29)]
# x = BitVec("x",8)
# s.add(~((~((~(x&64)) & x)) & (~((~(x&64)) & 64))) == 61)
# s.check()
# print(s.model())
# print(chr(125))
for i in range(29):
    regs[i] = flag[i]

while pc<0x2859:
    if ops[pc] == 1:
        t = (t - 1) % 0x40
        pc+=1
        continue
    else:
        print(pc,end=":")
    if ops[pc] == 0:
        print(f"regs[{(t+1)%0x40}] = {ops[pc+1]}")
        regs[(t+1)%0x40] = ops[pc+1]
        t=(t+1)%0x40
        pc+=2
        continue
    elif ops[pc] == 1:
        t=(t-1)%0x40
        pc+=1
        print("\r")
        continue
    elif ops[pc] == 2:
        print(f"regs[{(t+1)%0x40}] = regs[{t}]")
        regs[(t+1)%0x40] = regs[t]
        t=(t+1)%0x40
        pc+=1
        continue
    elif ops[pc] == 16:
        print(f"jz {pc + ops[pc-1]}")
        s.add(regs[t-1]==0)
        print(regs[t-1])
        print(s.check())
        print(s.model())
        pc += ops[pc-1]
        t-=1

        continue

        # if regs[t-1]==0:
        #     #jmp regs[t]
        #     pc += regs[t]
        #     t-=2
        # else:
        #     t -= 2
        #     pc+=1
        # t-=2
        # pc += 1
    elif ops[pc] == 18:
        print(f"jnz {pc + ops[pc-1]}")
        print(regs[t - 1])
        s.add(regs[t-1]==0)

        print(s.check())
        print(s.model())
        t-=2
        pc+=1
        continue

        # if regs[t-1]!=0:
        #     #jmp regs[t]
        #     pc += regs[t]
        #     t-=2
        # else:
        #     t -= 2
        #     pc+=1
        # t-=2
        # pc+=1
    elif ops[pc] == 32:
        print(f"add regs[{t-1}],regs[{t}]")
        regs[t - 1] = regs[t - 1] + regs[t]

        # if regs[t - 1] + regs[t] > 0xff:
        #     regs[t - 1] = -1
        # else:
        #     regs[t - 1] = regs[t - 1] + regs[t]
        t -= 1
        pc+=1
        continue
    elif ops[pc] == 33:
        print(f"sub regs[{t - 1}],regs[{t}]")
        regs[t-1] = regs[t] - regs[t - 1]
        # if regs[t] < regs[t - 1]:
        #     regs[t - 1] = 0
        # else:
        #     regs[t - 1] = regs[t] - regs[t - 1]
        t -= 1
        pc+=1
        continue
    elif ops[pc] == 34:
        print(f"mul regs[{t - 1}],regs[{t}]")
        regs[t - 1] = regs[t - 1] * regs[t]
        # if regs[t - 1] * regs[t] >> 8 != 0:
        #     regs[t - 1] = regs[t - 1] * regs[t]
        # else:
        #     regs[t - 1] = -1
        t -= 1
        pc+=1
        continue
    elif ops[pc] == 35:
        print(f"div regs[{t - 1}],regs[{t}]")

        regs[t - 1] = regs[t] // regs[t - 1]
        t -= 1
        pc+=1
        continue
    elif ops[pc] == 36:
        print(f"~(regs[{t - 1}]&regs[{t}])")

        regs[t - 1] = ~(regs[t] & regs[t - 1])
        t -= 1
        pc+=1
        continue
    elif ops[pc] == 66:
        print("read byte")
        pc+=1
        t+=1
        continue
    else:
        pc+=1
print(s.check())
