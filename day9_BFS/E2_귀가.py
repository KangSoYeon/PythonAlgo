from collections import deque

P = int(input())
#infos = [(lambda x:[x[0],x[1],int(x[2])]) (input().split()) for _ in range(P)]
arr_size = ord("z") + 1
arr = [[100002 for _ in range(arr_size)] for _ in range(arr_size)]
minDis = [100002 for _ in range(arr_size)]
que = deque()

for i in range(P):
    s, e, length = input().split()

    if int(length) < arr[ord(s)][ord(e)]:
        arr[ord(s)][ord(e)] = int(length)
        arr[ord(e)][ord(s)] = int(length)

que.append([ord("Z"), 0])
minDis[ord("Z")] = 0

while que:
    t, s = que.popleft()

    for i in range(0, arr_size):
        if arr[t][i] not in [100002, 0] and minDis[i] > s + arr[t][i]:
            que.append([i, s + arr[t][i]])
            minDis[i] = s + arr[t][i]

answer_min = min(minDis[:90])
print(chr(minDis.index(answer_min)), answer_min)