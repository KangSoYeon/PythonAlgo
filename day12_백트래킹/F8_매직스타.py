import sys

def input_data():
    readl = sys.stdin.readline
    map_star = [list(readl().strip()) for _ in range(5)]
    return map_star

# 입력받는 부분
star = input_data()
alpha = [False for _ in range(13)]
sum_list = [0 for _ in range(6)]
empty = []

for i in range(5):
    for j in range(8):
        if star[i][j] == 'x':
            empty.append([i, j])
            star[i][j] = 0

        elif star[i][j] == '.':
            continue
        else:
            temp = ord(star[i][j])-64
            alpha[temp] = True
            star[i][j] = temp

def check():

    if star[1][1] + star[2][2] + star[3][3] + star[4][4] > 26\
        or star[0][4] + star[1][3] + star[2][2] + star[3][1] > 26\
        or star[0][4] + star[1][5] + star[2][6] + star[3][7] > 26\
        or star[1][7] + star[2][6] + star[3][5] + star[4][4] > 26\
        or star[1][1] + star[1][3] + star[1][5] + star[1][7] > 26\
        or star[3][1] + star[3][3] + star[3][5] + star[3][7] > 26:

        return False

    return True


def dfs(c):

    if len(empty) == c:
        for i in range(5):
            for j in range(9):
                if star[i][j] == '.':
                    print(star[i][j], end='')
                else:
                    print(chr(star[i][j] + 64), end='')
            print()
        sys.exit()

    x, y = empty[c]

    #alpha[x][y] 에 1~12까지 넣어볼거임
    for i in range(1, 13):
        if alpha[i]: continue

        star[x][y] = i
        if not check():
            star[x][y] = 0
            continue

        alpha[i] = True

        dfs(c + 1)

        alpha[i] = False
        star[x][y] = 0

dfs(0)