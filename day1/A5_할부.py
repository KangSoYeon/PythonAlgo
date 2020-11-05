N = int(input())
B = int(input())

check = B / (N-1)
temp = B // (N-1)

maxD = B + temp
minD = maxD

if check == temp:
    minD = maxD - 1

print(minD, maxD, end=" ")


