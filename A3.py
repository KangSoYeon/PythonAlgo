N = int(input())
a = list(map(int, input().split()))

id_ = list(range(1, N+1))

for i in range(0,3):
    for j in range(i+1, N):
        if ((a[i] < a[j]) or (a[i] == a[j] and id_[i] > id_[j])):
            a[i], a[j] = a[j], a[i]
            id_[j], id_[i] = id_[i], id_[j]

for i in range(0,3):
    print(id_[i], end=" ")