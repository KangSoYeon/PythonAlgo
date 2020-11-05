import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info

sol = -1
# 입력받는 부분
N, info = input_data()

start, end = 301, 1130
# 여기서부터 작성
end = [0 for _ in range(1300)]

for i in info:
    s = i[0]*100 + i[1]
    e = i[2]*100 + i[3]

    end[s] = max(end[s], e)
    # for j in range(s, e):
    #     if end[j] < e:
    #         end[j] = e

s = 101
e = 302
latest = -1
answer = 0

while True:
    if e > 1130:
        break

    if s == e:
        s = e
        e = latest
        answer += 1
        continue

    if end[s] > latest:
        latest = end[s]
        print(s, e, latest)

    s += 1

print(answer)