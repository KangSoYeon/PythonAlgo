N = int(input())
a = list(map(int, input().split()))

for i in range(0, 4):
    for j in range(i+1, N):
        if a[i] > a[j] :
            a[i], a[j] = a[j], a[i]
        


for i in range(0, 4):
    print(a[i], end=" ")