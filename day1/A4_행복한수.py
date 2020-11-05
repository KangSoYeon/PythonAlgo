N = input()

def doubleInt(n) :
    answer = 0
    for i in range(len(n)):
        answer += int(n[i]) * int(n[i])

    return str(answer)


for i in range(int(N), 0, -1):
    check = [0 for i in range(1002)]
    check[i] += 1

    temp = doubleInt(str(i))

    check[int(temp)] += 1
    answer = 0

    while True:
        if temp == '1':
            answer = i
            break

        temp = doubleInt(temp)
        check[int(temp)] += 1

        if 2 in check:
            break

    if answer != 0:
        break

print(answer)