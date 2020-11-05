import sys

sudoku = [list(map(int, input().split())) for _ in range(9)]
x_check = [[True for _ in range(9)] for _ in range(9)]
y_check = [[True for _ in range(9)] for _ in range(9)]
square_check = [[True for _ in range(9)] for _ in range(9)]
empty = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            x_check[i][sudoku[i][j] - 1] = False
            y_check[j][sudoku[i][j] - 1] = False
            n = (i // 3) * 3 + (j // 3)
            square_check[n][sudoku[i][j] - 1] = False
        else:
            empty.append([i, j])

def dfs(c):
    global sudoku, empty

    if len(empty) == c:
        for i in sudoku:
            print(*i)
        sys.exit()

    x, y = empty[c]
    n = (x // 3) * 3 + (y // 3)

    for value in range(9):
        if not x_check[x][value]: continue
        if not y_check[y][value]: continue
        if not square_check[n][value]: continue

        x_check[x][value] = False
        y_check[y][value] = False
        square_check[n][value] = False
        sudoku[x][y] = value + 1

        dfs(c + 1)

        sudoku[x][y] = 0
        x_check[x][value] = True
        y_check[y][value] = True
        square_check[n][value] = True


dfs(0)