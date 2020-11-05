import sys

def input_data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N+1)]
    return N, W, H, info

# 입력받는 부분
N, W, H, info = input_data()

# 여기서부터 작성
# 왼쪽 위를 0으로 두고 절대 좌표 구하기
total_dist = 2*W + 2*H
dist = []
for i in info:
    if i[0] == 1:
        dist.append(i[1])
    elif i[0] == 2:
        dist.append(2 * W + H - i[1])
    elif i[0] == 3:
        dist.append(2 * W + 2 * H - i[1])
    else:
        dist.append(W + i[1])

dong = dist[N]
answer = 0
for i in range(N):
    temp = abs(dong - dist[i])
    answer += min(temp, total_dist-temp)

# 출력하는 부분
print(answer)