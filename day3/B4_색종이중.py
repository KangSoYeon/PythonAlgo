N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
board = [[0 for _ in range(102)] for _ in range(102)]
dir = [[0,1], [1,0], [-1,0], [0,-1]]
answer = 0

for i in info:
    for j in range(i[0], i[0]+10):
        for k in range(i[1], i[1]+10):
            board[j][k] = 1

for x, val in enumerate(board):
    for y, t in enumerate(val):
        if x == 0 or y == 0 or x == 101 or y == 101 : continue

        if t == 1:
            for k in dir:
                nx = x + k[0]
                ny = y + k[1]

                if board[nx][ny] == 0 : answer += 1

print(answer)