import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height

# 입력받는 부분
N, height = input_data()
sol_list = [0 for _ in range(N)]

stack = []
# 여기서부터 작성
for i, v in enumerate(height):
    count = 0
    for j in reversed(stack):
        if j[1] < v:
            count += 1
            sol_list[j[0]] = i+1
        else:
            break

    for tt in range(count): #답 구한만큼 스택 빼주기
        stack.pop()

    stack.append([i, v])

# 출력하는 부분
print(*sol_list, sep='\n')