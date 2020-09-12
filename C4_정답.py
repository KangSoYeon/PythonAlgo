from collections import deque

N, M = map(int, input().split())
s, e = [], []

for i in range(M) :
    a, b = map(int, input().split())
    s.append(a)
    e.append(b)

def bfs() :
    que = deque([1])
    visited = [1]

    while que:
        n = que.popleft()
        for i in range(M) :
            if s[i] == n and (e[i] not in visited) :
                que.append(e[i])
                visited.append(e[i])

            if e[i] == n and (s[i] not in visited) : #양방향이니까 두개 동시에 체크해줘야함
                que.append(s[i])
                visited.append(s[i])

    
    return visited

result = bfs()
for i in result:
    print(i, end=" ")
