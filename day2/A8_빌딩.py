N = int(input())

listN = []
strN = str(N)

for i in range(len(strN)):
    listN += strN[i]

for i in range(len(listN)):
    if int(listN[i]) > 4:
        listN[i] = str(int(listN[i]) - 1)

print(int(''.join(listN), 9))





