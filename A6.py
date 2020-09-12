N = int(input())
a = list(map(int, input().split()))
T = int(input())
b = list(map(int, input().split()))

def binary_search(target, data, N):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

for i in b: #찾아야하는 수
    idx = binary_search(i, a, N)
    if idx : 
        print(idx+1)
    else :
        print(0)
