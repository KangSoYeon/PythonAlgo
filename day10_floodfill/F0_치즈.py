from collections import deque

R, C = map(int, input().split())
map_ch = [list(map(int, input().split())) for _ in range(R)]
check = [[0 for _ in range(C)] for _ in range(R)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]

def bfs():
    que = deque([[0,0]])
    check[0][0] = -1

    while que:
        nx, ny = que.popleft()

        for d in dir:
            tx = nx + d[0]
            ty = ny + d[1]

            if 0<=tx<R and 0<=ty<C and check[tx][ty] == 0:
                if map_ch[tx][ty] > 0:
                    check[tx][ty] += 1
                else:
                    check[tx][ty] = -1
                    que.append([tx, ty])

time = 0
cheese = 0

while True:
    time += 1
    cheese = 0
    check = [[0 for _ in range(C)] for _ in range(R)]
    bfs()

    for i in range(R):
        for j in range(C):
            if check[i][j] > 0:
                map_ch[i][j] = 0 #치즈 녹이기
                cheese += 1

    flag = False
    for i in range(R):
        for j in range(C):
            if map_ch[i][j] == 1: #더이상 녹일 치즈가 없음
                flag = True

    if flag == False:
        break

print(time, cheese, sep="\n")