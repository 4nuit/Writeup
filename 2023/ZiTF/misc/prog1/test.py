grid = [['┌───┬───┬───┬───┬───┐'],
        ['│ x │ x │ x │ x │ x │'],
        ['├───┼───┼───┼───┼───┤'],
        ['│ x │ x │ x │ 0 │ x │'],
        ['├───┼───┼───┼───┼───┤'],
        ['│ x │ 5 │ 7 │ 6 │ x │'],
        ['├───┼───┼───┼───┼───┤'],
        ['│ x │ x │ x │ x │ 2 │'],
        ['├───┼───┼───┼───┼───┤'],
        ['│ x │ 4 │ x │ 1 │ 3 │'],
        ['└───┴───┴───┴───┴───┘']]

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
result = "|".join([f"{coord[0]},{coord[1]}" for _, coord in sorted(numbers)])
print(result)
