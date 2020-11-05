import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, edges

N, M, edges = input_data()
arr2 = [[0 for _ in range(N)] for _ in range(N)]

#인접행렬 만들기
for i in edges:
    A, B, edge = i
    arr2[A-1][B-1] = edge
    arr2[B-1][A-1] = edge

#arr를 체크하는 bfs
def bfs(arr):
    shortest = [[10000000, -1] for _ in range(N)] #쓰바 이 범위 초기화 때무네~~
    que = deque([[0, 0]])
    shortest[0] = [0, 0] #length, from

    while que:
        x, length = que.popleft()

        for i in range(N):
            if arr[x][i] != 0 and shortest[i][0] > (length + arr[x][i]):
                que.append([i, length + arr[x][i]])
                shortest[i] = [length + arr[x][i], x]

    return shortest

#초기값
dijk = bfs(arr2)
before = dijk[N-1][0]

idx = N-1
answer = -1
while True:
    length_, from_ = dijk[idx]

    arr2[idx][from_] *= 2
    arr2[from_][idx] *= 2

    after = bfs(arr2)[N - 1][0]
    answer = max(after-before, answer)

    arr2[idx][from_] = int(arr2[idx][from_]/2)
    arr2[from_][idx] = int(arr2[from_][idx]/2)

    idx = from_
    if idx == 0:
        break

print(answer)