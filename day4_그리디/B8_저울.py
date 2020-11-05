import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = list(map(int, readl().split()))
    return N, weight

sol = 0

# 입력받는 부분
N, weight = input_data()

# 여기서부터 작성
weight.sort()
sum = weight[0]

for i in range(1, len(weight)):
    if sum + 1 < weight[i]:
        break
    sum += weight[i]

sol = sum + 1

if weight[0] != 1:
    sol = 1

# 출력하는 부분
print(sol)