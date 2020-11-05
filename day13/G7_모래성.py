import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_sand = [list(readl()) for _ in range(R)]
    return R, C, map_sand

R, C, map_sand = input_data()

dir = [[1,0], [-1,0], [0,1], [0,-1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
que = deque([])

for i in range(R):
    for j in range(C):
        if map_sand[i][j] == '.':
            que.append([i, j])
        else:
            map_sand[i][j] = int(map_sand[i][j])

answer = 0
def bfs():
    global answer
    while que:
        size = len(que)
        answer += 1

        for _ in range(size):
            nx, ny = que.popleft()

            for d in dir:
                tx = nx + d[0]
                ty = ny + d[1]

                if 0<=tx<R and 0<=ty<C and map_sand[tx][ty] != '.':

                    map_sand[tx][ty] -= 1

                    if map_sand[tx][ty] == 0:
                        que.append([tx, ty])

bfs()
print(answer-1)