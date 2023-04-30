from Crypto.Random.random import randrange
from machine import Machine

def Fib(n):
    if n < 2:
        return n
    A = 0
    B = 1
    for _ in range(n - 1):
        C = A + B
        A = B
        B = C
    return B

def correctness(code):
    for _ in range(64):
        a = randrange(1024)
        c = Machine(code, a)  
        c.runCode()
        
        if c.error:
            print("[!] Error!")
            exit()

        if c.R0 != Fib(a):
            print("[!] Nope, you did not implement Fibonacci")
            exit()
    
    flag = open("flag.txt").read().strip()
    print(f"[+] Congrats! Here is the flag: {flag}")

if __name__ == "__main__":
    try:
        print("Enter your bytecode in hexadecimal:")
        code = input(">>> ")
        correctness(code)
    except:
        print("Please check your inputs.")
