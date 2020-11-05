# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N, S, M = map(int, readl().split())
    return N, S, M

sol_list = []

# 입력받는 부분
N, S, M = input_data()

# 여기서부터 작성
que = deque()
for i in range(S - 1, S + N - 1):
    que.append(i % N + 1)

while len(que) > 0:
	que.rotate(-(M-1))
	sol_list.append(que.popleft())

# 출력하는 부분
print(*sol_list)