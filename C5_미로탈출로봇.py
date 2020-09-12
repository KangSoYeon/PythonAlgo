from collections import deque

Y, X = map(int, input().split())
sy, sx, ey, ex = map(int, input().split())
arr = [list(map(int, input())) for i in range(X)]
visited = [[False] * Y for i in range(X)] #visited 배열 만들기

sx -= 1
sy -= 1
ex -= 1
ey -= 1

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# X, Y 뒤집혀 있어서 헷갈려죽음,, 입력만 거꾸로 받으면 됨..
#길: 0, 벽: 1
def bfs() :
    que = deque([[sx, sy]])
    visited[sx][sy] = True
    time = 0

    while que : #que가 있는동안
        size = len(que)
        time += 1

        for turn in range(size): 
            nx, ny = que.popleft()

            for i in range(len(dir)): #네방향으로 돌기
                tx = nx + dir[i][0]
                ty = ny + dir[i][1] 

                if tx >= 0 and tx < X and ty >= 0 and ty < Y and arr[tx][ty]==0 and visited[tx][ty]==False:    
                    if tx == ex and ty == ey : #도착하면 나오기
                        return time

                    que.append([tx, ty])
                    visited[tx][ty] = True

    return time

print(bfs())