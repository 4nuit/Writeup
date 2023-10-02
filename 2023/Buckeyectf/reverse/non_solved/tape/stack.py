import enum, string

class Op(enum.Enum):
    PUSH = 0
    POP = 1
    DUP = 2
    STDOUT = 0x40
    STDOUT_HEX = 0x41
    STDIN = 0x42
    STDIN_HEX = 0x43
    JMP = 0x10
    JNZ = 0x12
    ADD = 0x20
    SUBTRACT = 0x21
    MULTIPLY = 0x22
    DIVIDE = 0x23
    INVERT_W_MASK = 0x24
    EXIT = 0x50
prog = open('flag_checker', 'rb').read()






def get_success_jnz(in_rev):
    stack = [0xbb for _ in range(64)]
    ip = 0
    in_ = ''.join(in_rev[::-1])
    assert len(in_) == 29
    in_idx = 0
    success_count = 0
    while True:
        if ip >= len(prog):
            print('Out of bounds')
            break
        op = prog[ip]
        # print('==' * 64)
        # print(' '.join(list(map(lambda x: hex(x)[2:].zfill(2), stack))))

        assert len(stack) == 64
        match op:
            case Op.PUSH.value:
                stack = [prog[ip + 1]] + stack[:-1]
                ip += 2
            case Op.POP.value:
                stack = stack[1:] + [stack[0]]
                ip += 1
            case Op.DUP.value:
                stack = [stack[0]] + stack[:-1]
                ip += 1
            case Op.STDOUT.value:
                print(chr(stack[0]))
                ip += 1
            case Op.STDOUT_HEX.value:
                print(hex(stack[0]))
                ip += 1
            case Op.STDIN.value:
                stack = [ord(in_[in_idx])] + stack[:-1]
                in_idx += 1
                ip += 1
            case Op.STDIN_HEX.value:
                stack = [int(in_[in_idx], 16)] + stack[:-1]
                in_idx += 1
                ip += 1
            case Op.ADD.value:
                new_val = (stack[1] + stack[0]) & 0xff
                stack = [new_val] + stack[2:] + [stack[0]]
                ip += 1
            case Op.SUBTRACT.value:
                new_val = (stack[1] - stack[0]) & 0xff
                stack = [new_val] + stack[2:] + [stack[0]]
                ip += 1
            case Op.MULTIPLY.value:
                new_val = (stack[1] * stack[0]) & 0xff
                stack = [new_val] + stack[2:] + [stack[0]]
                ip += 1
            case Op.DIVIDE.value:
                new_val = (stack[1] // stack[0]) & 0xff
                stack = [new_val] + stack[2:] + [stack[0]]
                ip += 1
            case Op.INVERT_W_MASK.value:
                new_val = ~(stack[1] & stack[0]) & 0xff
                stack = [new_val] + stack[2:] + [stack[0]]
                ip += 1
            case Op.JMP.value:
                new_ip = ip + (stack[0] << 8 | stack[1])
                stack = stack[2:] + [stack[0], stack[1]]
                if new_ip >= len(prog):
                    ip += 1
                    print('Out of bounds JMP')
                else:
                    ip = new_ip
            case Op.JNZ.value:
                if stack[1] != 0:
                    # print('JNZ', hex(stack[1])[2:])
                    new_ip = ip + stack[0]
                    if new_ip >= len(prog):
                        ip += 1
                        # print('Out of bounds JNZ')
                    else:
                        ip = new_ip
                    return success_count
                else:
                    success_count += 1
                    # print('JNZ - NO JUMP')
                    ip += 1
                stack = stack[2:] + [stack[0], stack[1]]
            case Op.EXIT.value:
                break
            case _:
                print('Unknown opcode', hex(op))
                break
        # print(Op(op))
        # print(' '.join(list(map(lambda x: hex(x)[2:].zfill(2), stack))))
    print(in_[:in_idx+1])


pos = 0
best_success = 0
# bctf{y0u_Sp1n_M3_R1gHt_R0uNd}
in_rev = ['a' for _ in range(29)]

while True:
    for char in string.printable:
        in_rev[pos] = char
        success_rate = get_success_jnz(in_rev)
        if success_rate > best_success:
            best_success = success_rate
            pos += 1
            break
        print(''.join(in_rev[::-1]))