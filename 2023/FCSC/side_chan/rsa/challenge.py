# Python regular imports
import time
import gmpy2
from Crypto.Random.random import randrange

# Public files (challenge specific)
from machine import Machine
from rsa_keygeneration import RSAKeyGen

# Private files (challenge specific, server-side)
from attack import medium_attack, hard_attack

def correctness(code):
    m = 10619127615701520856379739649099426979408542335890705866261364729149521836708456587988611862249951573590276940006693869041738947270682165379632046509866331783356899823794403301245723493073492467753851795293781508164040007446360913101318418687822912180381048951020923643907154277561266233819048247765326638650752541513223846345841495736762626354734000304882818453092727291418557910284893185732873732411787817743633610538821430610661741018706699619754530233710049039412171314983572877330176030440604772328260918538377508345658521539614159242162939601919960471099651596787918311544317056893044464511883681887218275766883
    p = 169117692678049200091016180669291298820822047906774382397135930290030384240019313872407861054604570192861424905850899478040182931698465308015071359975759236483522841229524769531748108219440824747248912314870231953151380670803055367564376211721695404763143960627978376700754402905007977277024688827480296445319
    q = 94565767035691350451742458437489619502334958356686748610546575115051354834387574172318454287000873893169812442053035081377123072701019663233873224042166290287860699601481194460700512288806331512360426480451073999899179180858119250954071713594156778075850226522098319195392498992988718201923746162241303320983

    e = 2 ** 16 + 1
    dp = gmpy2.invert(e, p - 1)
    dq = gmpy2.invert(e, q - 1)
    iq = gmpy2.invert(q, p)
    d  = gmpy2.invert(e, (p - 1) * (q - 1))

    print("[+] Testing correctness...")

    c = Machine(code, m, p, q, iq, dp, dq, e, d)
    c.runCode()
    if c.error:
        print("[!] Error!")
        exit()

    sig = c.R0
    if sig != gmpy2.powmod(m, d, p * q):
        print(f"[!] Error: not functional! Got R0 = {sig}")
        exit()

    n, p, q, iq, dp, dq, d = RSAKeyGen(e, 2048)
    m = randrange(n)
    c = Machine(code, m, p, q, iq, dp, dq, e, d)
    c.runCode()
    sig = c.R0
    if m != gmpy2.powmod(sig, e, n):
        print("[!] Error: not functional!")
        exit()

    print("[+] Correct!")

def performances(code, max_ratio = 5/3):
    e = 2 ** 16 + 1
    n, p, q, iq, dp, dq, d = RSAKeyGen(e, 2048)
    m = randrange(n)

    def bench(code, num = 100):
        start = time.perf_counter_ns()
        for i in range(num):
            c = Machine(code, m, p, q, iq, dp, dq, e, d)
            c.runCode()
        end = time.perf_counter_ns()
        return (end - start) / num

    print("[+] Testing performances against the reference solution...")

    reference_solution = open("reference_solution.bytecode").read()
    perfSolution =   bench(reference_solution)
    perfSubmission = bench(code)

    print(f'[*] Reference performances: {perfSolution:7.2f} ns')
    print(f'[*] User performance:       {perfSubmission:7.2f} ns')
    print(f'[*] Ratio:                  {perfSubmission/perfSolution:7.2f}')
    
    if perfSubmission > max_ratio * perfSolution:
        print("[!] Error: too bad performances")
        exit()

def easy(code):
    correctness(code)
    performances(code)
    flag_easy = open("flag_easy.txt").read().strip()
    print(f"[+] Congrats! Here is the easy flag: {flag_easy}")

def medium(code):
    print("[*] Running attacks on your code when the machine is initialized without d.")
    check, t = medium_attack(code)
    if not check:
        print("[!] Nope! Your code is not secure enough.")
        return

    flag_medium = open("flag_medium.txt").read().strip()
    print(f"[+] Congrats! Here is the medium flag: {flag_medium}")

def hard(code):
    print("[*] Running attacks on your code when the machine is initialized without both e and d.")
    
    check, t = medium_attack(code)
    if not check:
        print("[!] Nope! Your code is not secure enough.")
        return

    check, t = hard_attack(code)
    if not check:
        print("[!] Nope! Your code is not secure enough.")
        return

    flag_hard = open("flag_hard.txt").read().strip()
    print(f"[+] Congrats! Here is the hard flag: {flag_hard}")

if __name__ == "__main__":

    try:
        print("Enter your bytecode in hexadecimal:")
        code = input(">>> ")

        while True:
            print("Which flag do you want to grab?")
            print("  0. Quit.")
            print("  1. Easy flag   - check for code correctness and performances.")
            print("  2. Medium flag - check resistance against several fault attacks, d not given.")
            print("  3. Hard flag   - check resistance against more fault attacks, not e and not d given.")
            choice = int(input(">>> "))

            if   choice == 0: exit()
            elif choice == 1: easy(code)
            elif choice == 2: medium(code)
            elif choice == 3: hard(code)

    except:
        print("Please check your inputs.")
