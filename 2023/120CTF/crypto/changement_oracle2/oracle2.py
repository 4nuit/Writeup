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
    print(f"Il y a eu quelques petits problèmes lors de ma précédente itération, mais tout a été résolu!\nJe peux à nouveau montrer mon secret sans craintes:\n{str(cipher)}\nPar mesure de sécurité, je ne peux malheureusement plus tout partager ici: \ne = {e}\n")
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
