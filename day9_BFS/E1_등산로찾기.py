from collections import deque

N = int(input())
x, y = map(int, input().split())
arr = [[0] + list(map(int, input().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
check = [[0] + [100000000] * N + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
que = deque([])

# 진입위치
for i in range(1, N+1):
    que.append([0, i])
    que.append([i, N+1])
    que.append([N+1, i])
    que.append([i, 0])

while que:
    nx, ny = que.popleft()

    for d in dir:
        tx = nx + d[0]
        ty = ny + d[1]

        if 1 <= tx <= N+1 and 1 <= ty <= N+1:
            new_power = check[nx][ny]

            if arr[tx][ty] < arr[nx][ny]:  # 낮아지면
                new_power += arr[nx][ny] - arr[tx][ty]

            elif arr[tx][ty] > arr[nx][ny]:
                new_power += ((arr[tx][ty] - arr[nx][ny]) ** 2)

            if new_power < check[tx][ty]:
                que.append([tx, ty])
                check[tx][ty] = new_power

print(check[x][y])