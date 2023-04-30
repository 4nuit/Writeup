import time
from Crypto.Random.random import randrange
from machine import Machine

def correctness(code):

    a = 1+randrange(65535)
    coin = 1
    c = Machine(code, a, a+a)
    c.runCode()
    
    if c.error:
        print("[!] Error!")
        exit()
        
    if c.R0 != coin:
        print("[!] Nope, you did not implement a comparison")
        exit()

    for _ in range(63):
        a = randrange(65536)
        b = a
        while a == b:
            b = randrange(65536)
        coin = randrange(2)
        if coin == 0:
            c = Machine(code, a, a)
        else:
            c = Machine(code, a, b)
        c.runCode()
        
        if c.error:
            print("[!] Error!")
            exit()
            
        if c.R0 != coin:
            print("[!] Nope, you did not implement a comparison")
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
