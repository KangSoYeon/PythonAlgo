R, C = map(int, input().split())
A = [[x for x in input()] for i in range(R)]

dir = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1, 1], [-1, -1]]

answer = []

for i in range(R):
    for j in range(C):
        if A[i][j]==".":
            temp = 0
            for k in range(8):
                dx = i + dir[k][0]
                dy = j + dir[k][1]
                if dx>=0 and dy>=0 and dx<R and dy<C:
                    if A[dx][dy]=="o":
                        temp += 1
            answer.append(temp)

print(max(answer))  

