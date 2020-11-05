import sys

def input_data():
    N = int(sys.stdin.readline())
    list_time = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    return N, list_time

sol = [-1, -1]

# 입력받는 부분
N, list_time = input_data()

# 여기서부터 작성
os, oe, xi, xe = 0, 0, 0, 0
start_sort = sorted(list_time, key=lambda t:t[0])

for idx, val in enumerate(start_sort):
    if idx == 0:
        os, oe = val[0], val[1]
        continue

    # 사람 있는 시간 유지
    if oe >= val[0]:
        #새로 들어온게 끝나는시간이 더 클때만
        if oe < val[1]:
            oe = val[1]

    # 사람있는 시간 끝
    else:
        xi, xe = oe, val[0]
        os, oe = val[0], val[1] #사람있는 시간 초기화 해야함

    if sol[0] < oe-os:
        sol[0] = oe-os

    if sol[1] < xe-xi:
        sol[1] = xe-xi

# 출력하는 부분
print(*sol)