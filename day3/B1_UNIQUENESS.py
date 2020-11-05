N = int(input())
words = input().split()
dic = {}
for i in range(len(words)):
    if words[i] in dic:
        dic[words[i]] += [i+1]
    else:
        dic[words[i]] = [i+1]

answer = ""

for key, value in dic.items():
    if len(value) > 1:
        answer += key + " "
        for j in value:
            answer += str(j) + " "
        answer += "\n"

if answer == "":
    answer = "unique"

print(answer)

