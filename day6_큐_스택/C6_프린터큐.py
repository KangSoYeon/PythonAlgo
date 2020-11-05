import sys

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    #입력받는 부분    
    N, M, job = input_data()
    pair = []
    result = []

    for i, v in enumerate(job):
        pair.append([i, v])

    while len(pair) > 1:
        turn = pair[0][1]
        flag = False
        for j in range(1, len(pair)):
            if pair[j][1] > turn:
                flag = True
                break

        popthis = pair.pop(0)

        if flag:
            pair.append(popthis)
        else:
            result.append(popthis)

    result += pair

    for i, v in enumerate(result):
        if v[0] == M:
            print(i+1)