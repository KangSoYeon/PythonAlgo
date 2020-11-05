import sys
from collections import deque

def input_data():
    L, R, C = map(int, readl().split())
    map_dungeon = [[list(readl().strip()) for r in range(R + 1)] for l in range(L)]
    return L, R, C, map_dungeon

readl = sys.stdin.readline

dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

while 1:
    # 입력 받는 부분
    L, R, C, map_dungeon = input_data()
    if L == 0 and R == 0 and C == 0: break

    # 여기서부터 작성
    for i in range(L):
        for j in range(R):
            for z in range(C):
                if map_dungeon[i][j][z] == 'S':
                    map_dungeon[i][j][z] = '.'
                    start = [i, j, z]
                elif map_dungeon[i][j][z] == 'E':
                    goal = [i, j, z]
                    map_dungeon[i][j][z] = '.'

    minutes = 0
    flag = False

    def bfs():
        global map_dungeon, minutes, flag
        que = deque([start])

        while que:
            size = len(que)

            for _ in range(size):
                nl, nx, ny = que.popleft()

                if [nl, nx, ny] == goal:
                    flag = True
                    return

                for d in dir:
                    tl = nl + d[0]
                    tx = nx + d[1]
                    ty = ny + d[2]

                    if 0<=tl<L and 0<=tx<R and 0<=ty<C \
                        and map_dungeon[tl][tx][ty]=='.':
                        que.append([tl, tx, ty])
                        map_dungeon[tl][tx][ty] = 'x' #갔던데 못가게 막기

            minutes += 1

    bfs()
    if flag:
        print("Escaped in " + str(minutes) + " minute(s).")
    else:
        print("Trapped!")




