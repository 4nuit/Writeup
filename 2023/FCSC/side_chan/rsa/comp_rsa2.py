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
; RC = d = exp
; RD = n = module

MOV R1, #200 ;r

;partie 1: s1_p
;q_prim = (q*r)%p
MUL R2, R7, R1
MOV RD, R6
MOD R2, R2

;q1 = m*pow(q_prim,e-2,p)
MOV R0, RB
MOV R3, #2
SUB R0, R0, R3
MOV RC, R0
POW R3, R2
MUL R3, R3, R5

;q2 = q1*pow(q_prim,2,p)
MOV RC, #2
POW R4, R2
MUL R4, R4, R3

;s1_p = q1*pow(q2,dp-1,p)
MOV R0, #1
MOV R2, R9
SUB R0, R2, R0 ; R0 = dp -1
MOV RC, R0
POW R0, R4
MUL R0, R0, R3 ; R0 = s1_p !!!

;partie 2: s1_q
; NE PAS ECRASER: R0,R1,R5,R6,R7
;p_prim = (p*r)%q
MUL R2, R6, R1
MOV RD, R7
MOD R2, R2

;p1 = m*pow(p_prim,e-2,q)
MOV R4, RB
MOV R3, #2
SUB R3, R4, R3
MOV RC, R3
POW R3, R2
MUL R3, R3, R5

;p2 = p1*pow(p_prim,2,q)
MOV RC, #2
POW R4, R2
MUL R4, R4, R3

;s1_q = p1*pow(p2,dq-1,q)
MOV R5, #1
MOV R2, RA
SUB R5, R2, R5 ; R5 = dq -1
MOV RC, R5
POW R2, R4
MUL R2, R2, R3 ; R2 = s1_q !!!

;s = (p*s1_q + q*s1_p)%n
; NE PAS ECRASER: R0,R1,R2,R6;R7
MUL R3, R6, R2
MUL R4, R7, R0

ADD R3, R3, R4
MUL R0, R6, R7 ;n dans RD
MOV RD, R0
MOD R3, R3 ; s dans R3

;r*s%n

MUL R0, R1, R3
MOD R0,R0

STP
	"""
	return compile(code)

stub()

