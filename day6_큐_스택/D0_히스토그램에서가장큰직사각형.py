import sys

def input_data():
    readl = sys.stdin.readline
    N, *list_height = map(int, readl().split())
    return N, list_height

while 1:
    # 입력받는 부분
    N, list_height = input_data()
    if N == 0: break

    stack = []
    answer = 0

    for i, v in enumerate(list_height):
        if i == 0:
            stack.append([i, v])
            continue

        if v < stack[-1][1]:
            min_idx = 0
            while len(stack) > 0 and stack[-1][1] > v:
                temp = stack.pop()
                if v < temp[1]:
                    space = (i - temp[0]) * temp[1]

                    if answer < space:
                        answer = space

                    min_idx = temp[0] #최저점 업데이트
                else:
                    break

            stack.append([min_idx, v])

        else:
            stack.append([i, v])

    while len(stack) > 0:
        temp = stack.pop()
        space = (N - temp[0]) * temp[1]

        if answer < space:
            answer = space

    print(answer)
