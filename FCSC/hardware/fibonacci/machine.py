import gmpy2
from Crypto.Util.number import GCD
from Crypto.Random.random import randrange

class Machine:
    def __init__(self, code, m = 0, p = 0, q = 0, iq = 0, dp = 0, dq = 0, e = 0, d = 0):
        self.a = 0
        self.b = 0
        self.R0 = 0
        self.R1 = 0
        self.R2 = 0
        self.R3 = 0
        self.R4 = 0
        self.R5 = m
        self.R6 = p
        self.R7 = q
        self.R8 = iq
        self.R9 = dp
        self.RA = dq
        self.RB = e
        self.exponent = d
        self.module = 0
        self.lr = -1
        self.pc = 0
        self.tokenizeCode(code)
        self.code_size = len(self.code)
        self.end = False
        self.error = False
        self.nbInstruction = 0

    def tokenizeCode(self,s):
        self.code = []
        if len(s) % 4 != 0:
            self.error = True
            return

        for i in range(len(s) // 4):
            self.code.append(s[4*i] + s[4*i + 1] + s[4*i + 2] + s[4*i + 3])

    def fetchInstruction(self):
        c = self.code[self.pc]
        opcode = int(c[0] + c[1], 16)
        operand1 = 0
        operand2 = 0

        # Case where the second byte contains only two operands
        if (0 << 6) == opcode & (3 << 6) or (2 << 6) == opcode & (3 << 6):
            operand1 = int(c[3], 16)
            operand2 = int(c[2], 16)
            self.dst = operand1

        # Case where b15 b14 b13 b12 b11 b10 b9 b8 b7 b6 b5 b4 b3 b2 b1 b0 => b13 b12 b11 b10 b9 is the instruction, b8 b7 b6 is the op2, b5 b4 b3 is the op1, b2 b1 b0 is the dst
        if (1 << 6) == opcode & (3 << 6):
            t        = int(c[1] + c[2] + c[3], 16)
            self.dst, t = 7 & t, t >> 3
            operand1, t = 7 & t, t >> 3
            operand2 = 7 & t
            opcode &= ((1 << 7) - 1) << 1

        if 0 == operand1:  self.a = self.R0
        if 1 == operand1:  self.a = self.R1
        if 2 == operand1:  self.a = self.R2
        if 3 == operand1:  self.a = self.R3
        if 4 == operand1:  self.a = self.R4
        if 5 == operand1:  self.a = self.R5
        if 6 == operand1:  self.a = self.R6
        if 7 == operand1:  self.a = self.R7
        if 8 == operand1:  self.a = self.R8
        if 9 == operand1:  self.a = self.R9
        if 10 == operand1: self.a = self.RA
        if 11 == operand1: self.a = self.RB
        if 12 == operand1: self.a = self.exponent
        if 13 == operand1: self.a = self.module
        if 14 == operand1: self.a = self.lr
        if 15 == operand1: self.a = self.pc

        if 0 == operand2:  self.b = self.R0
        if 1 == operand2:  self.b = self.R1
        if 2 == operand2:  self.b = self.R2
        if 3 == operand2:  self.b = self.R3
        if 4 == operand2:  self.b = self.R4
        if 5 == operand2:  self.b = self.R5
        if 6 == operand2:  self.b = self.R6
        if 7 == operand2:  self.b = self.R7
        if 8 == operand2:  self.b = self.R8
        if 9 == operand2:  self.b = self.R9
        if 10 == operand2: self.b = self.RA
        if 11 == operand2: self.b = self.RB
        if 12 == operand2: self.b = self.exponent
        if 13 == operand2: self.b = self.module
        if 14 == operand2: self.b = self.lr
        if 15 == operand2: self.b = self.pc

        # Case where the instruction is on 4 bytes
        if (2 << 6) == opcode & (3 << 6) :
            self.pc += 1
            self.b = int(self.code[self.pc], 16)
            opcode = opcode & ((1 << 7)-1)

        # Case where the second byte represents an 8-bit value
        if (3 << 6) == opcode & (3 << 6):
            self.b = int(c[2] + c[3], 16)

        self.instruction = False

        if 0 == opcode:               self.instruction = self.move
        if (0 + (2 << 6)) == opcode:  self.instruction = self.move
        if (0 + (1 << 6)) == opcode:  self.instruction = self.log_and
        if (2 + (1 << 6)) == opcode:  self.instruction = self.log_or
        if (4 + (1 << 6)) == opcode:  self.instruction = self.log_xor
        if (6 + (1 << 6)) == opcode:  self.instruction = self.shiftL
        if (8 + (1 << 6)) == opcode:  self.instruction = self.shiftR
        if 1 == opcode:               self.instruction = self.bit_len
        if (10 + (1 << 6)) == opcode: self.instruction = self.add
        if (12 + (1 << 6)) == opcode: self.instruction = self.sub
        if (14 + (1 << 6)) == opcode: self.instruction = self.mul
        if (16 + (1 << 6)) == opcode: self.instruction = self.div
        if 2 == opcode:               self.instruction = self.mod
        if 3 == opcode:               self.instruction = self.pow
        if (18 + (1 << 6)) == opcode: self.instruction = self.gcd
        if 4 == opcode:               self.instruction = self.invert
        if 5 == opcode:               self.instruction = self.random
        if 6 == opcode:               self.instruction = self.cmp

        # relative jumps have an odd opcode
        if 7 == opcode or ((3 << 6) + 7) == opcode:   self.instruction = self.jz_rel
        if 8 == opcode or ((2 << 6) + 8) == opcode:   self.instruction = self.jz_abs
        if 9 == opcode or ((3 << 6) + 9) == opcode:   self.instruction = self.jnz_rel
        if 10 == opcode or ((2 << 6) + 10) == opcode: self.instruction = self.jnz_abs
        if 11 == opcode or ((3 << 6) + 11) == opcode: self.instruction = self.jc_rel
        if 12 == opcode or ((2 << 6) + 12) == opcode: self.instruction = self.jc_abs
        if 13 == opcode or ((3 << 6) + 13) == opcode: self.instruction = self.jnc_rel
        if 14 == opcode or ((2 << 6) + 14) == opcode: self.instruction = self.jnc_abs
        if 15 == opcode or ((3 << 6) + 15) == opcode: self.instruction = self.j_rel
        if 16 == opcode or ((2 << 6) + 16) == opcode: self.instruction = self.j_abs
        if 17 == opcode or ((3 << 6) + 17) == opcode: self.instruction = self.call_rel
        if 18 == opcode or ((2 << 6) + 18) == opcode: self.instruction = self.call_abs
        if 19 == opcode:                              self.instruction = self.ret
        if 20 == opcode:                              self.instruction = self.stop
        if 21 == opcode:                              self.instruction = self.movc
        if 22 == opcode:                              self.instruction = self.movcb
        if 23 == opcode:                              self.instruction = self.movcw

        self.pc += 1
        if not self.instruction:
            self.error = True

    def executeInstruction(self):
        if not self.error:
            self.instruction()

    def runCode(self):
        while True:
            t = self.pc
            self.fetchInstruction()
            self.executeInstruction()

            self.nbInstruction += 1
            if self.end or self.error:
                return self

            if self.pc >= self.code_size or self.nbInstruction > (1 << 16):
                self.end = True
                self.error = True
                return self

    def finalize_move(self):
        if 0 == self.dst:  self.R0 = self.a
        if 1 == self.dst:  self.R1 = self.a
        if 2 == self.dst:  self.R2 = self.a
        if 3 == self.dst:  self.R3 = self.a
        if 4 == self.dst:  self.R4 = self.a
        if 5 == self.dst:  self.R5 = self.a
        if 6 == self.dst:  self.R6 = self.a
        if 7 == self.dst:  self.R7 = self.a
        if 8 == self.dst:  self.R8 = self.a
        if 9 == self.dst:  self.R9 = self.a
        if 10 == self.dst: self.RA = self.a
        if 11 == self.dst: self.RB = self.a
        if 12 == self.dst: self.exponent = self.a
        if 13 == self.dst: self.module = self.a
        if 14 == self.dst: self.lr = self.a
        if 15 == self.dst: self.pc = self.a

    def move(self):
        self.a = self.b
        self.finalize_move()

    def log_and(self):
        self.a = self.a & self.b
        self.finalize_move()

    def log_or(self):
        self.a = self.a | self.b
        self.finalize_move()

    def log_xor(self):
        self.a = self.a ^ self.b
        self.finalize_move()

    def shiftL(self):
        self.a = self.a  <<  self.b
        self.finalize_move()

    def shiftR(self):
        self.a = self.a >> self.b
        self.finalize_move()

    def bit_len(self):
        self.a = self.b.bit_length()
        self.finalize_move()

    def add(self):
        self.a = self.a + self.b
        self.finalize_move()

    def sub(self):
        self.C = (self.a >= self.b)
        self.Z = (self.a == self.b)
        self.a = self.a - self.b
        self.finalize_move()

    def mul(self):
        self.Z = (self.a == 0 or self.b == 0)
        self.a = self.a * self.b
        self.finalize_move()

    def div(self):
        if self.b != 0:
            self.a = self.a // self.b
            self.finalize_move()
        else:
            self.error = True

    def mod(self):
        self.a = self.b % self.module
        self.finalize_move()

    def pow(self):
        self.a = gmpy2.powmod(self.b, self.exponent, self.module)
        self.Z = (self.a == 0)
        self.finalize_move()

    def gcd(self):
        self.a = GCD(self.a, self.b)
        self.finalize_move()

    def invert(self):
        if 1 == GCD(self.b, self.module):
            self.a = gmpy2.powmod(self.b, -1, self.module)
            self.finalize_move()
        else:
            self.error = True

    def random(self):
        if 0 == self.a:
            self.error = True
            return
        if self.a <= (1 << 12):
            self.a = randrange(2 ** (8 * self.a))
            self.finalize_move()

    def cmp(self):
        self.C = (self.a >= self.b)
        self.Z = (self.a == self.b)

    def jz_rel(self):
        if self.Z:
            if self.b < (1 << 7):
                self.pc += self.b
            else:
                self.pc -= (1 << 8) - self.b

    def jnz_rel(self):
        if not self.Z:
            if self.b < (1 << 7):
                self.pc += self.b
            else:
                self.pc -= (1 << 8) - self.b

    def jc_rel(self):
        if self.C:
            if self.b < (1 << 7):
                self.pc += self.b
            else:
                self.pc -= (1 << 8) - self.b

    def jnc_rel(self):
        if not self.C:
            if self.b < (1 << 7):
                self.pc += self.b
            else:
                self.pc -= (1 << 8) - self.b

    def jz_abs(self):
        if self.Z:
            self.pc = self.b

    def jnz_abs(self):
        if not self.Z:
            self.pc = self.b

    def jc_abs(self):
        if self.C:
            self.pc = self.b

    def jnc_abs(self):
        if not self.C:
            self.pc = self.b

    def j_rel(self):
        if self.b < (1 << 7):
            self.pc += self.b
        else:
            self.pc -= (1 << 8) - self.b

    def j_abs(self):
        self.pc = self.b

    def call_rel(self):
        self.lr = self.pc
        if self.b < (1 << 7):
            self.pc += self.b
        else:
            self.pc -= (1 << 8) - self.b

    def call_abs(self):
        self.lr = self.pc
        self.pc = self.b

    def ret(self):
        self.pc = self.lr

    def stop(self):
        self.end = True

    def movcw(self):
        c= self.code[self.a]
        self.a = int(c[0:4],16)
        self.finalize_move()

    def movc(self):
        t = 0
        for i in range(self.b):
            c = self.code[self.a+i]
            t <<= 16
            t ^= int(c[0:4], 16)
        self.a = t
        self.finalize_move()
