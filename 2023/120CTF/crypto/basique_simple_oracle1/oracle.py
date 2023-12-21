from Crypto.Util.number import bytes_to_long, getStrongPrime, inverse
from inputimeout import inputimeout, TimeoutOccurred
from .flag import flag
import signal

def main():
    e = 0x10001
    p,q = getStrongPrime(1024), getStrongPrime(1024)
    N = p * q
    d = inverse (e, (p-1) * (q-1))
    cipher = pow(bytes_to_long(flag), e, N)
    print(f"Voici le message secret que je dois garder. Vous pouvez le voir, de toute façon vous ne pourrez rien en faire!\n{str(cipher)}\nJ'en profite également pour noter quelques informations ici: \nN = {N}\ne = {e}\n")
    print("Ceci étant dit, passons à ce que vous vouliez me dire!\n")
    while True:
        try:
            a = inputimeout(prompt="> ", timeout=60)
        except:
            exit(1)
        try:
            inp = int(a)
            if inp % N == cipher:
                print("Je refuse de répondre à ceci\n")
            else:
                ans = pow(inp, d, N)
                print(f"Voici ma réponse:\n{str(ans)}\n")
        except Exception as e:
            print("Je ne répond qu'au nombres entiers \n")
            continue

def handler(signum, frame):
    exit(1)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(600)
    main()
