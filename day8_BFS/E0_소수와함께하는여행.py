from collections import deque
import copy

S, E = map(list, input().split())
S, E = list(map(int, S)), list(map(int, E))
check = [False for _ in range(0, 10000)]
answer = 0
def primecheck(a):

    arr = [True] * a

    m = int(a ** 0.5)
    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(i+i, a, i):
                arr[j] = False

    return [i for i in range(999, a) if arr[i] == True]

primeList = primecheck(10002)


def bfs():
    global answer, E
    que = deque([S])
    tt = int(''.join(map(str, S)))
    check[tt] = True
    flag = False

    while que:
        if flag: break
        size = len(que)
        answer += 1

        for repeat in range(size):
            t = que.popleft()
            flag = False
            if t == E:
                flag = True
                break

            for i in range(4):
                for j in range(0, 10): # 다 바꿔보기
                    copyOne = copy.deepcopy(t)
                    if i == 0 and j == 0: continue

                    if j != copyOne[i]:
                        copyOne[i] = j

                    toNum = int(''.join(map(str, copyOne)))

                    if (toNum in primeList) and check[toNum] == False:
                        que.append(copyOne)
                        check[toNum] = True


bfs()
print(answer-1)