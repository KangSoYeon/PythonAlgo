
def search(score, cnt):
    global result
    if cnt == 15:
        if score == answer:
            result = 1
        return

    for i in range(18):
        if score[i] > answer[i]:
            return

    A = round[cnt][0]
    B = round[cnt][1]

    score[A*3] += 1
    score[B*3+2] += 1
    search(score, cnt+1)
    score[A*3] -= 1
    score[B*3+2] -= 1

    score[A*3+1] += 1
    score[B*3+1] += 1
    search(score, cnt + 1)
    score[A*3+1] -= 1
    score[B*3+1] -= 1

    score[A*3+2] += 1
    score[B*3] += 1
    search(score, cnt + 1)
    score[A*3+2] -= 1
    score[B*3] -= 1


possible = []
for tc in range(4):
    answer = list(map(int, input().split()))
    result = 0
    round = []

    for i in range(5):
        for j in range(i+1, 6):
            round.append((i, j))

    search([0]*18, 0)
    possible.append(result)

print(*possible)