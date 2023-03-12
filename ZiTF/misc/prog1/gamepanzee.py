from pwn import *

conn = remote('10.0.0.4', 8095)
print(conn.recvline())
conn.recvuntil(b'Difficulty:\n')
conn.sendline(b'1')
print(conn.recvuntil(b'Game starts in 0\n'))

# Extraire la grille
grid = []
for i in range(10):
    line = conn.recvline().decode().strip()
    row = [c.strip() for c in line.split('|')]
    grid.append(row)

print(grid)

new_grid = []
for row in grid:
    new_row = []
    for item in row[0]:
        if item == 'x' or item.isdigit():
            new_row.append(item)
    new_grid.append(new_row)

new_grid = [row for row in new_grid if row]; print(new_grid)

numbers = []
for i in range(len(new_grid)):
    for j in range(len(new_grid[i])):
        if new_grid[i][j].isdigit():
            numbers.append([int(new_grid[i][j]), (i+1, j+1)])

print(numbers)
result = "|".join([f"{coord[0]},{coord[1]}" for _, coord in sorted(numbers)]); print(result)

conn.sendline(result.encode())

print(conn.recvline())
conn.close()
