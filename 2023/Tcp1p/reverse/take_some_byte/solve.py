from z3 import *

# Créez un solveur
solver = Solver()

# Créez un tableau de variables BitVec pour chaque position du flag
flag = [BitVec(f'flag_{i}', 32) for i in range(25)]

# Ajoutez des contraintes pour les caractères ASCII imprimables (32 à 127)
for i in range(25):
	solver.add(And(flag[i] >= 32, flag[i] <= 127))

# Ajoutez les contraintes spécifiques pour votre problème
solver.add(flag[0:6] == [ord('T'), ord('C'), ord('P'), ord('1'), ord('P'), ord('{')])
solver.add(flag[-1] == ord('}'))
solver.add(flag[6:10] == [ord('b'), ord('y'), ord('t'), ord('e')])
solver.add(flag[10] == ord('_'))
solver.add(flag[11:15] == [ord('c'), ord('o'), ord('d'), ord('e')])
solver.add(flag[15] == ord('_'))
solver.add(flag[16:19] == [ord('i'), ord('s'), ord('_')])
solver.add(flag[19] == ord('H'))
solver.add(flag[20] == 117)
solver.add(flag[21] - flag[22] == 10)
solver.add(flag[23] == ord('B'))
solver.add(flag[24] == flag[23])

while True:
	# Vérifiez si le solveur a une solution
	if solver.check() == sat:
		model = solver.model()
		flag_chars = [chr(model[flag[i]].as_long()) for i in range(25)]
		flag_solution = "".join(flag_chars)
		print("Flag trouvé:", flag_solution)
	else:
		print("Aucune solution trouvée")
