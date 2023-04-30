from assembly import assembly

source=""

def compile(code):
	global source
	source = code
	z = assembly(code.upper().split('\n'))
	print(code)
	print("[",z,"]")
	return z.encode()

def stub():
	code = f"""
; R5 = m
; R6 = p
; R7 = q
; R8 = iq = q**(-1) % p
; R9 = dp = e**(-1) % p-1
; RA = dq = e**(-1) % q-1
; RB = e
; RC = d
; RD = n

; dp en exp
; p en mod
MOV RC, R9
MOV RD, R6
POW R1, R5 ;s1 = m**dp %p

; dq en exp
; q en mod
MOV RC, RA
MOV RD, R7
POW R2, R5 ;s2 = m**dp %q

; p en mod
; s1-s2 dans R3
; iq*(s1-s2) dans R4 
; h = iq*(s1-s2) %p dans R0
MOV RD, R6
SUB R3, R1, R2
MOV R4, R8
MUL R3, R4, R3 ;ATTENTION : R[0-7] pour MUL
MOD R3, R3

; s2 + hq dans R0
MUL R1, R3, R7
ADD R0, R2, R1

STP
	"""
	return compile(code)

stub()

