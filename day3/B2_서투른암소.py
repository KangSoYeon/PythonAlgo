N = list(input())

stack = []
answer = 0

for i in N:
    if i == "(":
        stack.append(i)
    else:
        if len(stack) == 0:
            answer += 1
            stack.append("(")
        else:
            stack.pop()

if len(stack) != 0:
    answer += len(stack) / 2

print(int(answer))







