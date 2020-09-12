from collections import deque

N, M = map(int, input().split())
array = [[0] * (N + 1) for i in range(N + 1)]

for i in range(M) :
    a, b = map(int, input().split())
    array[a][b] = 1
    array[b][a] = 1

def bfs() :
    visited = [1]
    queue = deque([1])

    while queue:
        n = queue.popleft()
        for idx in range( N+1 ):
            if array[n][idx] == 1 and (idx not in visited):
                queue.append(idx)
                visited.append(idx)
    return visited

result = bfs()
for i in result:
    print(i, end=" ")



