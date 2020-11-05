import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    chems = [list(map(int,readl().split())) for _ in range(N)]
    return N, chems

sol = 1

# 입력받는 부분
N, chems = input_data()

chems.sort()
s, e = chems[0]

for i in chems:
    if i == 0 : continue

    if i[0] <= e:
        if e > i[1]:
            e = i[1]
    else:
        sol += 1
        s, e = i

print(sol)
