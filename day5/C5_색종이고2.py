N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
board = [[0 for _ in range(102)] for _ in range(102)]

for i in info:
    for j in range(i[0], i[0] + 10):
        for k in range(i[1], i[1] + 10):
            board[j][k] = 1

max_paper = 0
for i, value in enumerate(board):
    for j, v in enumerate(value):

        if v == 1:
            tc, tr = 0, 0
            tc2, tr2 = 0, 0
            while True:
                if board[i + tc][j] == 0:
                    break
                tc += 1

            while True:
                if board[i][j + tr] == 0:
                    break
                tr += 1

            flag = False
            for t1 in range(i, 101):
                for t2 in range(j, i+tr):
                    if board[t1][t2] == 0:
                        flag = True
                        break

                if flag: break
                tr2 += 1

            flag = False
            for t1 in range(j, 101):
                for t2 in range(i, i + tc):
                    if board[t1][t2] == 0:
                        flag = True
                        break

                if flag: break
                tc2 += 1

            max_paper = max(tc * tc2, tr * tr2, max_paper)

print(max_paper)