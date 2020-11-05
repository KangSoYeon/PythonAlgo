N, P = map(int, input().split())
arr = [0 for i in range(P+1)]

def getCur(p):
    return (N*p) % P;

temp = N
for i in range(P*P):
    temp = getCur(temp)
    arr[temp] += 1

answer = 0
for i in arr:
    if i > 1:
        answer += 1

print(answer)