N = int(input())   
a = list(map(int, input().split()))

a.sort()

for item in a:
    print(item, end=' ')
