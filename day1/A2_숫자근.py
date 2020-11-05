N = int(input())
arr = [0 for i in range(N)]

for i in range(N):
    arr[i] = int(input())

def getSum(a):
    answer = 0
    if int(a) >= 10:
        for i in a:
            answer += int(i)

    return str(answer)

max = 0
idx = 0
for i in range(len(arr)):
    temp = getSum(str(arr[i]))

    while True:
        if int(temp) < 10:
            break
        temp = getSum(str(temp))

    if int(temp) > max:
        max = int(temp)
        idx = i
    elif int(temp) == max:
        if arr[i] < arr[idx]:
            idx = i

print(arr[idx])