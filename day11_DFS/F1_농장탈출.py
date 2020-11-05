import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight

def check(a, b):
    size = len(a)
    if len(a) > len(b):
        size = len(b)

    a = a[::-1]
    b = b[::-1]
    for i in range(size):
        if int(a[i]) + int(b[i]) > 9:
            return False

    return True

# s: 태우기 시도할 소 시작 index
# cnt: 태운 소의수
# sum_weight: 태운 소의 무게값

def dfs(s, cnt, sum_weight):
    global sol
    # 현제 진행중인 경우의 수가 5마리를 태웠고 앞으로 태울수 있는 소가 3마리 남았습니다.
    # 그런데 지금까지 확인된 최고 탑승 소의 수가 8개 입니다...
    # #그렇다면 현재 경우의 수는 앞으로 진행시켜서 아무리 많은 소를 태운다 하더라도 최대 8마리이죠.
    # 지금까지 확인된 상황보다 더 좋은 케이스를 찾을 수는 없는 경우의 수라고 생각할 수 있죠.
    # N-s : 앞으로 최대한 태울 수 있는 소의 수

    if cnt + (N - s) <= sol:
        return
    sol = max(sol, cnt)
    for n in range(s, N):
        if check(str(sum_weight), str(weight[n])):
            dfs(n + 1, cnt + 1, sum_weight + weight[n])

sol = -1
# 입력받는 부분
N, weight = input_data()

# 여기서부터 작성
sol = 0
dfs(0, 0, 0)

# 출력하는 부분
print(sol)