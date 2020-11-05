map_bingo = [list(map(int, input().split())) for _ in range(5)]
seq_bingo = []
for _ in range(5):
    seq_bingo += list(map(int, input().split()))

flag = [0 for i in range(12)]
position = [0 for i in range(26)]
answer = 0

#요소별 인덱스 관리 따로하기
for i in range(len(map_bingo)):
    for j in range(len(map_bingo[i])):
        position[map_bingo[i][j]] = [i, j]

#하나씩 지우기
for i in seq_bingo:
    answer += 1
    x = position[i][0]
    y = position[i][1]

    flag[x] += 1
    flag[y+5] += 1

    if x-y == 0:
        flag[-1] += 1
    if x+y == 4:
        flag[-2] += 1

    if flag.count(5) >= 3:
        break

print(answer)