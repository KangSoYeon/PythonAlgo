import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    K = int(readl())
    pos = [[0] * N for _ in range(N)]

    for i in range(K):
        y, x = map(int, readl().split())
        pos[y - 1][x - 1] = 1
    pos[0][0] = 2

    L = int(readl())
    cmd_list = []
    for i in range(L):
        t, k = readl().split()
        cmd_list.append([int(t), k])

    return N, K, pos, L, cmd_list

# 입력받는 부분
N, K, pos, L, cmd_list = input_data()

# 여기서부터 작성
length = 1
y, x, d, time = 0, 0, 0, 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
key = [dy[d], dx[d]]
snake = [[y, x]]

while True:
    flag = True
    if cmd_list:
        k = cmd_list.pop(0)
    else:
        k = 0,0
    while time != k[0]:

        y += key[0]
        x += key[1]
        if y < 0 or x < 0 or y >= N or x >= N:
            print(time+1)
            flag = False
            break
        if pos[y][x] == 2:
            print(time+1)
            flag = False
            break

        snake.append([y, x])
        if pos[y][x] == 0:
            ny, nx = snake.pop(0)
            pos[ny][nx] = 0
        pos[y][x] = 2
        time += 1

    if k[1] == 'D':
        d = (d + 1) % 4
    elif k[1] == 'L':
        d = (d - 1) % 4
    key = [dy[d], dx[d]]

    if not flag:
        break

if flag:
    print(time)