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

redo:

    ;ja player_one

    ;mov R0,#0
    ;mov RB, R0
    ;mov RC, R0


    mov R0, RC  ; d préchargé
    mov R1, RB ; e préchargé

    mov R4, #0

    cmp R0, R4 ; d==0 ?
    JZA no_d
    cmp R1,R4  ; d with no e?
    jZa no_e_but_d
    ja have_de

    
no_d:


    ; pas de d, est ce grave?
    cmp R1,R4 ; e==0 ?
    JZA no_de ; ni d ni e

    JA k_epq ; pas grave on va reconstruire tout ca (sauf d)

    
no_de:
ja fin

    ; ni d ni e, ca va etre sportif
    mov R0,#10
    ja fin

    
no_e_but_d:

    ; d in R0
    ; a priori suffit d'avoir pq dp dq
    mov R4, #1      ;1
    mov R2, R6
    mov R1, R7
    sub R2, R2, R4  ; p-1
    sub R1, R1, R4  ; q-1

    mul R3, R2, R1    ;phi = (p-1)(q-1)
    mov RD, R3
    inv R4,R0  ;e = inv(d,phi)


    mov RB, R4
    ; ayé on a d et e
    mov R4,R0 ; sauvons ce d

    mov RD, R2
    mod R3,R4 ; dp=  d%(p - 1)
    mov R9,R3

    mov RD, R1
    mod R3,R4 ; dq=  d%(q - 1)
    mov RA,R3

    JA player_one

    
    
have_de:

    ; on a a et d
    ;ja no_e_but_d ; on n'a pas confiance

    ja k_epq   ; x1.96 x1.34

    ja player_one ; on a confiance (x1.12)

    
k_epq:

    mov R0, RB
    mov RC,R0   ;  =========> init exp

    mov R0, R6
    mov R1, R7
    mul R4, R0, R1  ; n
    mov RD, R4    ; ========> init modulo n

    mov R4, #1      ;1
    sub R0, R0, R4  ; p-1
    sub R1, R1, R4  ; q-1
    mov R4, RB


    mov RD, R0
    inv R3,R4 ; dp=  gmpy2.invert(e, p - 1)
    mov R9,R3

    mov RD, R1
    inv R3,R4 ; dq=  gmpy2.invert(e, q - 1)
    mov RA,R3


    ja player_one

    

e_404:
    ; on s'est perdu, somehow
    mov R0, #404
    ja fin
player_one:

    



    mov R8,#64 ;512    ; 8 ok
    RND R8       ; R8 est la variable r

   




    ;mov RB,  RC  ; on sauve e => verif qu'ensuite personne n'y touche


    ; building S1P build_calcSP("R3","R8","R6","R7","R9","R1","RB")


    
    mov RD, R6                ; positionnement de l'exposant pour tout le reste

    mov R1, R8
    mul R1, R7, R1
    mod R4, R1         ; qp = (q*r) %p

    mov R1, #2         ; tmp=2
    mov R0, RB    ; tmp2=e
    sub R1, R0, R1  ; tmp = tmp2-tmp = e-2

    mov RC, R1  ; exp = e-2
    pow R2, R4      ; pow(qp,e-2,p)
    mul R2, R5, R2
                                ; q1 = m*pow(qp,e-2,p)


    
    mov R1,#2
    mov RC, R1  ; exp = 2
    pow R4, R4                                              ;= dernier usage de QP R4
    mul R4, R2, R4              ; q2 = q1*pow(qp,2,p)


    mov R1,#1
    mov R0,R9       ; passage ephemere par R0
    sub R1, R0, R1    ;dp-1
    mov RC, R1            ; exp = dp-1
    pow R1, R4             ; pow(q2,dp-1,p)

    mul R1, R2, R1
    mod R3, R1                ; S1p = (q1*pow(q2,dp-1,p))%p


    ; return S1p
    

    ; S1P dispo dans R3

    mov R9, R3
    ; building S1Q build_calcSP("R2","R8","R7","R6","RA","R1","RB")
    
    mov RD, R7                ; positionnement de l'exposant pour tout le reste

    mov R1, R8
    mul R1, R6, R1
    mod R4, R1         ; qp = (q*r) %p

    mov R1, #2         ; tmp=2
    mov R0, RB    ; tmp2=e
    sub R1, R0, R1  ; tmp = tmp2-tmp = e-2

    mov RC, R1  ; exp = e-2
    pow R2, R4      ; pow(qp,e-2,p)
    mul R2, R5, R2
                                ; q1 = m*pow(qp,e-2,p)


    
    mov R1,#2
    mov RC, R1  ; exp = 2
    pow R4, R4                                              ;= dernier usage de QP R4
    mul R4, R2, R4              ; q2 = q1*pow(qp,2,p)


    mov R1,#1
    mov R0,RA       ; passage ephemere par R0
    sub R1, R0, R1    ;dp-1
    mov RC, R1            ; exp = dp-1
    pow R1, R4             ; pow(q2,dp-1,p)

    mul R1, R2, R1
    mod R2, R1                ; S1p = (q1*pow(q2,dp-1,p))%p


    ; return S1p
    

    ; S1Q dispo dans R2
    mov RA, R2


    mov R0, R6        ;p
    mov R1, R7       ;q
    mul R1, R1, R0  ; n=p*q
    mov RD, R1    ; Reset de n en modulo global

    mov R1, R7
    mul R3, R3, R1 ; q*S1p => ici on perd S1p qui n'est plus used ensuite

    mod R3, R3

    mov R1, R6
    mul R2, R2, R1 ; p*S1q => ici on perd S1q qui n'est plus used ensuite
    mod R2, R2



    add  R1, R2, R3    ;S = (p*S1q + q*S1p)%n
    mod R0, R1  ; ok  S = (p*S1q + q*S1p)%n
    mov R1, R8
    mul R0, R0, R1
    mod R0,R0

    mov RC, RB
    pow R1, R0
    cmp R1, R5
    JNCA redo
    ;JNCA error1
    ;check=pow((r*S),e,n)-m
    

new2:
    ja fin



error1:
    mov R0,#1
    ja fin


fin:

STP
	"""
	return compile(code)

stub()

