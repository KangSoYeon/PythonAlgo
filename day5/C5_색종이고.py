N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
board = [[0 for _ in range(102)] for _ in range(102)]
up = []
down = []

sol = 0

info.sort()

for i in info:
    for j in range(i[0], i[0]+10):
        for k in range(i[1], i[1]+10):
            if j > k:
                up.append([j,k])
            else:
                down.append([j,k])

            board[j][k] = 1

def checkPaper(start, end):

    for i in range(start[0], end[0]+1):
        for j in range(start[1], start[1]+1):
            if board[i][j] == 0:
                return 0

    return (abs(start[0] - end[0])+1) * (abs(start[1] - end[1])+1)



for i in up:
    for j in down:

        chk = checkPaper(i, j)

        if sol < chk:
            sol = chk

print(sol)
