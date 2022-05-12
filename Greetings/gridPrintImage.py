grid = []
grid2 = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#Create a custom grid
for i in range(10):
    grid.append(['  x  '])
    for y in range (10):
        grid[i].append('  x  ')

#Print grid 
for i in range(6):
    for y in range(9):
        print(grid2[y][i], end='')
    print()

    print()