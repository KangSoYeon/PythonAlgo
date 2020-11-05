N, str_org = input().split()

level = [[] for _ in range(100)]
stack = []

str_org = str_org.replace("<", " < ")
str_org = str_org.replace(">", " > ")
s = str_org.split()

idx = 0
for i in s:
    if i == "<":
        stack.append(i)
    elif i == ">":
        stack.pop()
    else:
        level[idx].append(i)

    idx = len(stack)

print(*level[int(N)])