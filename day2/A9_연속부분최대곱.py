N = int(input())
num = [float(input()) for _ in range(N)]

mul = 1
max = 0
#누적으로 곱을 구해가는데, 누적값이 1보다 작으면 다시 셈
for i in num:
    if mul < 1:
        mul = i
    else:
        mul *= i

    if mul > max:
        max = mul

print(format(max, ".3f"))