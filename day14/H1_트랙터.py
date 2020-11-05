import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_field = [[9999999] + list(map(int, readl().split()))  + [9999999] if 1<=r<=N else [9999999] * (N+2)  for r in range(N+2)]
    return N, map_field


sol = -1
# 입력받는 부분
N, map_field = input_data()

# 여기서부터 작성
print(N)
print(map_field)

# 출력하는 부분
print(sol)