import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M

# 입력받는 부분
N, needs, M = input_data()

#parametric search 쓰기

# 여기서부터 작성
max_val = max(needs)
total = M

while len(needs) > 0:
    average = int(total / len(needs))
    flag = False
    for i in reversed(range(len(needs))):
        if needs[i] <= average:
            total -= needs.pop(i)
            flag = True

    if not flag: break #더이상 줄일 수 없음

if max_val < average:
    print(max_val)
else:
    print(average)
