import sys
import bisect

def input_data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals
sol = 0

# 입력받는 부분
M, N, L, shoots, animals = input_data()

animals.sort(key=lambda x: x[0])
shoots.sort()

# 여기서부터 작성
for i in animals:
    gap = L - i[1]
    if gap < 0 : continue

    s = i[0] - gap
    e = i[0] + gap

    #사대 안에서 s, e 찾기
    start = bisect.bisect_left(shoots, s)
    end = bisect.bisect_right(shoots, e)

    print(start, end)

    if start != end:
        sol += 1

# 출력받는 부분
print(sol)