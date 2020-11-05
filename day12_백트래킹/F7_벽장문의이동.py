import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    A, B = map(int, readl().split())
    S = int(readl())
    seq = [int(readl()) for _ in range(S)]
    return N, A, B, S, seq

#입력받는 부분
N, A, B, S, seq = input_data()

answer = 999999999999
# 여기서부터 작성
def dfs(a, b, target_idx, cnt):

    global answer
    if target_idx >= S:
        answer = min(answer, cnt)
        return

    #a 바꾸기
    dfs(seq[target_idx], b, target_idx + 1, cnt + abs(a-seq[target_idx]))
    #b 바꾸기
    dfs(a, seq[target_idx], target_idx + 1, cnt + abs(b-seq[target_idx]))


dfs(A, B, 0, 0)
print(answer)