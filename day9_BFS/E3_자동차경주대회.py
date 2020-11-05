import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    L = int(readl())
    N = int(readl())
    dist = [0] + list(map(int, readl().split()))
    time = [0] + list(map(int, readl().split())) + [0]
    return L, N, dist, time

# 입력받는 부분
L, N, dist, time = input_data()

# 여기서부터 작성
def bfs():
    que = deque([[[0], 0]]) #track[], total
    min = sys.maxsize
    answer = []
    min_arr = [min for _ in range(N+2)]
    min_arr[0] = 0

    while que:
        track, total = que.popleft()
        cur_dist = 0

        for i in range(track[-1] + 1, N + 2):
            cur_dist += dist[i]
            if cur_dist <= L:
                if min_arr[i] > total + time[i]:
                    que.append([track + [i], total + time[i]])
                    min_arr[i] = total + time[i]
                    answer = track + [i]
            else:
                break

        # print(que)
        # print(min_arr)

    return answer, min_arr[N+1] #마지막꺼 뽑았어야해,,,

if L >= sum(dist):
    print(0)

else:
    ans, m = bfs()

    print(m)
    print(len(ans)-2)
    print(*ans[1:-1])