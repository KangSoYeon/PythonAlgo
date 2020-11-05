import sys
from copy import deepcopy

def input_data():
    map_soli = [list(readl().strip()) for _ in range(5)]
    readl()
    return map_soli

readl = sys.stdin.readline
T = int(input())
dir = [[1,0], [0,1], [-1,0], [0,-1]]

def dfs(cnt, b):
    global remain, total_time
    flag = False

    for i in range(5):
        for j in range(9):
            if b[i][j] == 'o':
                for d in range(4):
                    tx = i + dir[d][0]
                    ty = j + dir[d][1]

                    ntx = i + (dir[d][0] * 2)
                    nty = j + (dir[d][1] * 2)

                    if 0 <= ntx < 5 and 0 <= nty < 9:
                        if b[tx][ty] == 'o' and b[ntx][nty] == '.':
                            newBoard = deepcopy(b)
                            newBoard[i][j] = '.'
                            newBoard[tx][ty] = '.'
                            newBoard[ntx][nty] = 'o'
                            flag = True
                            dfs(cnt + 1, newBoard)

    if not flag:
        temp = 0
        for i in range(5):
            for j in range(9):
                if b[i][j] == 'o':
                    temp += 1

        if temp < remain:
            remain = temp
            total_time = cnt
        elif temp == remain and cnt < total_time:
            total_time = cnt

for test_case in range(T):

    board = input_data()

    remain = 1000000
    total_time = 99999999999999

    dfs(0, board)
    print(remain, total_time)