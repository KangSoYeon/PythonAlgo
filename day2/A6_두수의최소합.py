N = int(input())
arr = list(map(int, input().split()))

arr.sort()
a = ""
b = ""

# 0의 갯수만큼 두개 뒤로 빼기
temp = arr.count(0)
arr2 = arr[temp:temp+2] + arr[:temp] + arr[temp+2:]

for i in range(len(arr2)):
    if i % 2 == 0:
        a += str(arr2[i])
    else:
        b += str(arr2[i])

print(int(a) + int(b))
