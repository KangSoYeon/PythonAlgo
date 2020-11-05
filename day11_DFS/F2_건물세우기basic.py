import copy
N = int(input())
cost = [list(map(int, input().split())) for n in range(N)]

temp_list = [0 for _ in range(N)]
visited = [False for _ in range(N)]

answer = 100000000000
answer_list = []

def dfs(idx, val):
    global answer, answer_list

    if val > answer: # 가지치기 안해주면 터짐
        return

    if idx >= N:
        if answer > val:
            answer = val
            answer_list = copy.deepcopy(temp_list)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            temp_list[i] = idx + 1
            dfs(idx + 1, val + cost[i][idx])
            visited[i] = False

dfs(0, 0)

print(answer)
print(*answer_list)