import sys

def input_data():
    readl = sys.stdin.readline
    B, N = map(int, readl().split())
    weight_ship = [int(readl()) for _ in range(B)]
    weight_passenger = [0] + [int(readl()) for _ in range(N)]
    return B, N, weight_ship, weight_passenger

sol = -0x7fffffff

# 입력받는 부분
B, N, weight_ship, weight_passenger = input_data()

# 여기서부터 작성


# 출력하는 부분
print(sol)