import time
import random
from math import gcd

def lrac(x):
    """Racine carrée entière d'un nb entier x (méth. de Héron d'Alexandrie)"""
    r1 = 1
    while True:
        r2 = (r1+x//r1)//2 
        if abs(r1-r2) < 2:
            if r1*r1 <= x and (r1+1)*(r1+1) > x:
                return r1
        r1 = r2

def _millerRabin(a, n):
    """Ne pas appeler directement (fonction utilitaire). Appeler millerRabin(n, k=20)"""
    # trouver s et d pour transformer n-1 en (2**s)*d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
 
    apow = pow(a,d,n) 
 
    # si (a**d) % n ==1 => n est probablement 1er
    if apow == 1:
        return True
 
    for r in range(0,s):
        # si a**(d*(2**r)) % n == (n-1) => n est probablement 1er
        if pow(a,d,n) == n-1:
            return True
        d *= 2
 
    return False
 
# ========================
petitspremiers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
    79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
    179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,
    269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,
    367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,
    461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,
    571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,
    661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,
    773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,
    883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,]
# ========================

def estpremier(n, k=20):
    """Test de primalité probabiliste de Miller-Rabin"""
    global petitspremiers
 
    # éliminer le cas des petits nombres <=1024
    if n<=1024:
        if n in petitspremiers:
            return True
        else:
            return False
 
    # éliminer le cas des nombres pairs qui ne peuvent pas être 1ers!
    if n & 1 == 0:
        return False
 
    # recommencer le test k fois: seul les nb ayant réussi k fois seront True
    for repete in range(0, k):
        # trouver un nombre au hasard entre 1 et n-1 (bornes inclues)
        a = random.randint(1, n-1)
        # si le test echoue une seule fois => n est composé
        if not _millerRabin(a, n):
            return False
    # n a réussi les k tests => il est probablement 1er
    return True

def facteursdiv2(n):
    """Décomposition par division de n (entier) en 2 facteurs quelconques"""
    pp = [2, 3, 5, 7, 11]
    racn = lrac(n)+1  # lrac(n) = racine carrée entière de n
    for p in pp:
        if p>racn:
            return [n, 1]  # n est premier
        if n%p == 0:
            return [p, n//p]  # on a trouvé une décomposition
    p = pp[-1] + 2
    while p <= racn:
        if n%p == 0:
            return [p, n//p]  # on a trouvé une décomposition
        p += 2
    # si on arrive ici, n est premier
    return [n, 1]
 
def pollardrho(n):
    """Factorisation d'un nombre entier décomposable (méth. rho de pollard)"""   
    f = lambda z: z*z+1
    x, y, d = 2, 2, 1
    while d==1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(x-y, n)
    return [d, n//d]
 
def factpremiers(n):
    """liste des facteurs premiers de n, avec la fonction 'a, b = decomp(n)' """
    R = []  # liste des facteurs premiers trouvés
    P = [n]  # pile de calcul
    while P!=[]:
        x = P.pop(-1)  # lecture et dépilage de la dernière valeur empilée
        if estpremier(x):
            R.append(x)  # on a trouvé un facteur 1er => on ajoute à la liste
        else:
            a, b = pollardrho(x)  # on calcule une nouvelle décomposition
            if a==1 or b==1:
                # echec: x n'est pas 1er mais sa decomposition ne se fait pas
                # on essaie une décomposition par division
                a, b = facteursdiv2(x)
            P.append(a)  # on empile a
            P.append(b)  # on empile b
    R.sort()
    return R

n=274590119602335071883284727412187324226799161489160216918946541623962023898947462941162730504512877671091317387950219158091491477787906472877937527736500927827788160999948998539494618780154007025505324811223950077056222454280253397798437155895137195235121334866176325410590511959827261043282130460056449720245009165808554755421956804092315137742989228976124850046926175777482964585472546165980711950730324854377458099096828685232308528920010463829909123873856338613070273045846729458753746791212393780647435164237423230876460579166121024778182453807467266812414479402615672127245661404527505635074780168541710026342597
274590119602335071883284727412187324226799161489160216918946541623962023898947462941162730504512877671091317387950219158091491477787906472877937527736500927827788160999948998539494618780154007025505324811223950077056222454280253397798437155895137195235121334866176325410590511959827261043282130460056449720245009165808554755421956804092315137742989228976124850046926175777482964585472546165980711950730324854377458099096828685232308528920010463829909123873856338613070273045846729458753746791212393780647435164237423230876460579166121024778182453807467266812414479402615672127245661404527505635074780168541710026342597
#print(n)

start = time.time()
result=factpremiers(n)
print(len(result))
end = time.time()

print(result)
elapsed = end - start
print(f'Temps d\'exécution : {elapsed:.2}s')
