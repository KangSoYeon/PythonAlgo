from collections import deque

T = int(input())
dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]

for testcase in range(T):
    C, R = map(int, input().split())
    arr, S, D, checked = [], [], [], [[False for _ in range(R)] for _ in range(C)]
    que = deque()
    time = 0

    for i in range(C):
        arr.append(list(input()))

    for i in range(C):
        for j in range(R):

            if arr[i][j] == "S":
                S = [i, j]
                arr[i][j] = "0"
                checked[i][j] = True
            elif arr[i][j] == "D":
                D = [i, j]
            elif arr[i][j] == "*":  # 홍수 확산 먼저
                que.append([i, j])
                checked[i][j] = True


    def bfs():
        global que
        que.append(S)  # 화가 위치 나중에

        while que:
            nx, ny = que.popleft()

            for d in dir:
                tx = nx + d[0]
                ty = ny + d[1]

                if 0 <= tx < C and 0 <= ty < R and checked[tx][ty] == False:
                    if arr[nx][ny] == "*":
                        if arr[tx][ty] not in ["X", "D"]:
                            arr[tx][ty] = "*"
                            que.append([tx, ty])
                            checked[tx][ty] = True

                    elif arr[nx][ny] not in [".", "X", "D", "S", "*"]:  # 화가의 위치이면
                        if arr[tx][ty] not in ["X", "*"]:
                            arr[tx][ty] = str(int(arr[nx][ny]) + 1)
                            que.append([tx, ty])
                            checked[tx][ty] = True

    bfs()

    if arr[D[0]][D[1]] == "D":
        print("KAKTUS")
    else:
        print(arr[D[0]][D[1]])