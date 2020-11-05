from collections import deque
M, N, K = map(int, input().split())
rects = [list(map(int, input().split())) for _ in range(K)]
arr = [[0 for _ in range(N)] for _ in range(M)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]

for i in rects:
    sy, sx, ey, ex = i
    for tx in range(sx, ex):
        for ty in range(sy, ey):
            arr[tx][ty] = -1

def bfs(i, j, val):
    answer = 0
    que = deque([[i, j]])
    arr[i][j] = val

    while que:
        nx, ny = que.popleft()
        answer += 1
        for d in dir:
            tx = nx + d[0]
            ty = ny + d[1]

            if 0<=tx<M and 0<=ty<N and arr[tx][ty] == 0:
                que.append([tx, ty])
                arr[tx][ty] = val

    return answer

total = 0
space = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            total += 1
            space.append(bfs(i, j, total))

print(total)
print(*sorted(space))