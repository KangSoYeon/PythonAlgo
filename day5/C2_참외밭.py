import sys

def input_data():
    readl = sys.stdin.readline
    K = int(readl())
    edges = [list(map(int,readl().split())) for _ in range(6)]
    return K, edges

sol = 0
K, edges = input_data()

# 여기서부터 작성
row, col = [], []
for idx, i in enumerate(edges):
    if i[0] < 3:
        row.append([idx, i[0], i[1]])
    else:
        col.append([idx, i[0], i[1]])

max_row = max(row, key=lambda x: x[2])
max_col = max(col, key=lambda x: x[2])

# 계산식 맞게 정렬
if max_row[0] - max_col[0] == 1:
    edges = edges[max_row[0]:] + edges[:max_col[0] + 1]
elif max_col[0] - max_row[0] == 1:
    edges = edges[max_col[0]:] + edges[:max_row[0] + 1]

sol = ((edges[0][1] * edges[1][1]) + (edges[3][1] * edges[4][1])) * K

# 출력하는 부분
print(sol)