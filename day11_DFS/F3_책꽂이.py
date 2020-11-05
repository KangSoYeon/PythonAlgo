import sys

def input_data():
    N, B = map(int, readl().split())
    height = [int(readl()) for _ in range(N)]
    return N, B, height

readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    N, B, height = input_data()
    # 여기서부터 작성
    answer = 999999999
    def dfs(idx, s):
        global answer
        if s >= B: #끝
            if answer > s-B:
                answer = s-B
            return

        if idx >= N:
            return

        dfs(idx + 1, s + height[idx])
        dfs(idx + 1, s)

    dfs(0, 0)
    print(answer)