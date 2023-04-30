r = 2371   #rand
q = 17
m = 3
p = 19
e = 65537
phi = (p-1)*(q-1)
d = pow(e,-1,phi)

n = p*q
dp = pow(e,-1,p-1)
dq = pow(e,-1,q-1)

# algo

q_prim = (q*r)%p
q1 = m*pow(q_prim,e-2,p)
q2 = q1*pow(q_prim,2,p)
s1_p = (q1*pow(q2,dp-1,p)) #%p

p_prim =  (p*r)%q
p1 = m*pow(p_prim,e-2,q)
p2 = p1*pow(p_prim,2,q)
s1_q = (p1*pow(p2,dq-1,q)) #%q

s = (p*s1_q + q*s1_p)%n

print(pow(r*s,e,n)%n)
print(m)

# On veut r*s%n
print("signature oberthur:", r*s%n)
print("signature classique:",pow(m,d,n))