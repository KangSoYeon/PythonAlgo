import sys

def input_data():
    readl = sys.stdin.readline
    K = int(readl())
    N = int(readl())
    info = [readl().split() for _ in range(N)]
    info = [(int(t), z) for t,z in info]
    return K, N, info

K, N, info = input_data()
sol = 0

def solve():
    totalTime = 0
    turn = 0

    for i in info:
        totalTime += i[0]
        if totalTime >= 210:
            break

        if i[1] == 'T':
            turn += 1

    answer = K + turn

    if K + turn > 8:
        answer = (K + turn) % 8

    return answer

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(sol)