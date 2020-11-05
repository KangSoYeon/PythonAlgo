import sys

def input_data():
    readl = sys.stdin.readline
    N, C = map(int, readl().split())
    M = int(readl())
    info = [list(map(int, readl().split())) for _ in range(M)]

    return N, C, M, info

sol = 0

# 입력받는 부분
N, C, M, info = input_data()

arr = sorted(info, key=lambda x:(x[1], x[0]))
capa = [C] * N

for idx, v in enumerate(arr):
    remain = v[2]

    for i in range(v[0], v[1]):
        if capa[i] < remain:
            remain = capa[i]

    for i in range(v[0], v[1]):
        capa[i] -= remain

    sol += remain

# 출력하는 부분
print(sol)