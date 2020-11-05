from collections import deque
N = int(input())
arr = [[0 for _ in range(102)] for _ in range(102)]
check = [[False for _ in range(102)] for _ in range(102)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]

for i in range(N):
    x, y = map(int, input().split())
    arr[x][y] = 1

def bfs():
    que = deque([[0, 0]])
    check[0][0] = True
    answer = 0

    while que:
        nx, ny = que.popleft()
        #빼서 테두리 1인거 체크
        for d in dir:
            tx = nx + d[0]
            ty = ny + d[1]

            # 하나하나 0에 사방을 체크하면서 1과 맞닿은 갯수 세기
            if 0 <= tx < 102 and 0 <= ty < 102 and arr[tx][ty] == 1:
                answer += 1

        #0인것들은 다 넣기
        for d in dir:
            tx = nx + d[0]
            ty = ny + d[1]

            if 0<=tx<102 and 0<=ty<102 and arr[tx][ty] == 0 and check[tx][ty] == False:
                    que.append([tx, ty])
                    check[tx][ty] = True

    return answer

print(bfs())