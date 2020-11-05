import copy
from collections import deque

R, C = map(int, input().split())
arr = []
for i in range(C):
    arr.append(list(map(int, input())))
sr, sc = map(int, input().split())

sr -= 1
sc -= 1
sol_time, sol_zergling = 3, 0
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = copy.deepcopy(arr)

#저글링 총 수 세기
for i in range(C):
    for j in range(R):
        if arr[i][j] == 1:
            sol_zergling += 1

def bfs():
    global sol_zergling, sol_time
    que = deque([[sc, sr]])
    visited[sc][sr] = 3

    while que:
        nx, ny = que.popleft()
        sol_zergling -= 1 #죽인 저글링 수만큼 세기

        for d in dir:
            tx = nx + d[0]
            ty = ny + d[1]

            if 0 <= tx < C and 0 <= ty < R and arr[tx][ty] == 1 and visited[tx][ty] == 1:
                que.append([tx, ty])
                visited[tx][ty] = visited[nx][ny] + 1
                if sol_time < visited[tx][ty]: #가장 큰 죽는시간 업데이트
                    sol_time = visited[tx][ty]

bfs()

# 출력하는 부분
print(sol_time, sol_zergling, sep='\n')