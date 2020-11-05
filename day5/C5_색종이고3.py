N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 102 for i in range(102)]
max_cnt = 100

for i in info:
    for j in range(i[0], i[0] + 10):
        for k in range(i[1], i[1] + 10):
            board[j][k] = 1


def checkPaper(start, end):
    global max_cnt
    for i in range(end[0], start[0], -1):
        for j in range(end[1], start[1], -1):
            if max_cnt >= (i - start[0]) * (j - start[1]): continue

            flag = True
            for k in range(start[0], i):
                for m in range(start[1], j):

                    if board[k][m] == 1: continue

                    else:
                        flag = False
                        break
            if flag:
                max_cnt = (i - start[0]) * (j - start[1])
                break


for i in range(102):
    for j in range(102):

        if board[i][j] == 1:

            for k in range(i, 100):
                if board[k][j] == 0:
                    break

            for m in range(j, 100):
                if board[i][m] == 0:
                    break

            if max_cnt < (k - i) * (m - j):
                checkPaper((i, j), (k, m))

print(max_cnt)