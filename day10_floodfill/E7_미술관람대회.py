from collections import deque
N = int(input())
map_nor_pig = [list(input()) for r in range(N)]
check = [[False for _ in range(N)] for _ in range(N)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]

def bfs(que, value):
    while que:
        size = len(que)

        for turn in range(size):
            nx, ny = que.popleft()

            for d in dir:
                tx = nx + d[0]
                ty = ny + d[1]

                if 0<=tx<N and 0<=ty<N and check[tx][ty] == False and map_nor_pig[tx][ty]==value:
                    que.append([tx, ty])
                    check[tx][ty] = True

original_pig = 0
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            original_pig += 1
            check[i][j] = True
            que = deque([[i, j]])
            bfs(que, map_nor_pig[i][j])


dis_pig = 0
#적록색맹 처리
for i in range(N):
    for j in range(N):
        if map_nor_pig[i][j] == 'G':
            map_nor_pig[i][j] = 'R'

check = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            dis_pig += 1
            check[i][j] = True
            que = deque([[i, j]])
            bfs(que, map_nor_pig[i][j])

print(original_pig, dis_pig)

