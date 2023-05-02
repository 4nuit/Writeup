import csv

def exp_by_squaring(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exp_by_squaring(x * x, n // 2)
    else:
        return x * exp_by_squaring(x * x, (n - 1) // 2)

trace_admin = []
with open('trace_admin.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        trace_admin.append(float(row[0]))

trace_user = []
with open('trace_utilisateur.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        trace_user.append(float(row[0]))

for n in range(len(trace_admin)):
    if exp_by_squaring(2, n) == 2727955623:
        print(f"Exposant trouvé : {n}")
        break
