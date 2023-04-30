#à modifier
#créer sa propre liste
#{Maj-Mins-Maj}-3chiffres-@#
#         |
#         |
#nomanimal|
import hashlib
HASH = 'ca868318d6a3283d089377545a7c3275be934177d9946aba86638b658bae131e'
def main():
        with open("/usr/share/wordlists/rockyou.txt", mode="r", encoding= 'utf-8') as PASSLIST:
                for line in PASSLIST:
                        line = line.rstrip("\r\n")
                        word = (f'{line+"@#"}')
                        guess = hashlib.sha256(word.encode('utf-8')).hexdigest()
                        if guess.upper() == HASH or guess.lower() == HASH:
                                print(f'[+] Password found: {word}')
                                exit(0)
                        else:
                                print(f'[-] Guess: {word} incorrect... {guess}')
                print(f'Password not found in wordlist...')
if __name__ == '__main__':
        main()
