import os

def usage():
	print('Actions possibles:')
	print('  - "comparer X Y": compare les valeurs du tableau aux cases X et Y, et retourne 1 si la valeur en X est inférieure ou égale à celle en Y, 0 sinon.')
	print('  - "echanger X Y": échange les valeurs du tableau aux cases X et Y, et affiche le taleau modifié.')
	print('  - "longueur:       retourne la longueur du tableau.')
	print('  - "verifier:      retourne le flag si le tableau est trié.')

def printArray(A):
	print(" ".join("*" for a in A))

def verifier(A):
	return all([ A[i] <= A[i + 1] for i in range(len(A) - 1) ])

if __name__ == "__main__":

	A = list(os.urandom(32))
	print("Votre but est de trier un tableau dont vous ne voyez pas les valeurs (chacune est remplacée par *) :")
	printArray(A)
	usage()
	B = A[:]

	try:
		nbCmp = 5 * 32 + 25
		while True:
			x = input(">>> ")

			if x.startswith("comparer"):
				if nbCmp > 0:
					x, y = list(map(int, x.split(" ")[1:]))
					print(int(A[x] <= A[y]))
					nbCmp -= 1
				else:
					print("Erreur : plus de comparaisons disponibles !")
			
			elif x.startswith("echanger"):
				x, y = list(map(int, x.split(" ")[1:]))
				A[x], A[y] = A[y], A[x]

			elif x.startswith("longueur"):
				print(len(A))

			elif x.startswith("verifier"):
				c = verifier(A)
				if c:
					flag = open("flag.txt").read().strip()
					print(f"Le flag est : {flag}")
				else:
					print("Erreur : le tableau n'est pas trié")
					print(f"Le tableau de départ était : {B}")
					print(f"Le tableau final est :       {A}")
				print("Bye bye!")
				break

			else:
				usage()
	except:
		print("Erreur : vérifier les commandes envoyées.")

