N = list(input())
idx = 0
answer = 0

#여는괄호가 많으면 닫는괄호 많은 모양으로 뒤집어 버리기
if N.count("(") > N.count(")"):
     for i in range(len(N)):
         if N[i] == "(":
             N[i] = ")"
         else:
             N[i] = "("
     N.reverse()

for i in N:
    if i == "(":
        idx += 1
    else:
        answer += 1
        idx -= 1

    if idx < 0:
        break

#같은 경우는 무시~
if N.count("(") == N.count(")"):
    answer = 0

print(answer)
