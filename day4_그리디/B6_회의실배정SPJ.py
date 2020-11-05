import sys

def input_data():
    N = int(sys.stdin.readline())
    list_meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    return N, list_meeting

# 입력받는 부분
N, list_meeting = input_data()

# 여기서부터 작성
arrange_meeting = sorted(list_meeting, key=lambda x: x[2])

cnt = 0
occupy = ""
overtime = 0
for idx, val in enumerate(arrange_meeting):
    if idx == 0:
        cnt += 1
        occupy += str(val[0]) + " "
        overtime = val[2]

    else:
        if val[1] >= overtime:
            cnt += 1
            occupy += str(val[0]) + " "
            overtime = val[2]
        else:
            continue

# 출력하는 부분
print(cnt)
print(occupy)