N, P = map(int, input().split())

temp = list(range(1, N))
answer = list()


for i in range(0, N//2):
    idx = 0
    answer[idx].append(temp[i])
    answer[idx+=1]


