import sys

def input_data():
    A, N = map(int, readl().split())
    W = list(map(int, readl().split()))
    return A, N, W

readl = sys.stdin.readline
T = int(readl())
for t in range(1, T+1):
    # 입력받는 부분
    A, N, W = input_data()

    # 여기서부터 작성
    W.sort()
    answer = 999999999999

    def dfs(me, idx, cnt):
        global answer

        if me == 1: # 1일땐 N이 답
            answer = N
            return

        if idx >= N: #끝까지 돌았을떄  종료
            answer = min(cnt, answer)
            return

        if cnt > answer: # 최소 answer을 넘어서 들어갈 때
            return

        if W[idx] < me:
            dfs(me + W[idx], idx+1, cnt)
        else:
            dfs(me*2-1, idx, cnt+1)
            dfs(me, idx+1, cnt+1)

    dfs(A, 0, 0)
    print("Case #"+ str(t)+": "+str(answer))
