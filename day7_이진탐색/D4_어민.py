import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info

sol = -1

# 입력받는 부분
N, info = input_data()

info.sort(key=lambda x:(x[0], x[1]))

# 여기서부터 작성





# 출력하는 부분
print(sol)