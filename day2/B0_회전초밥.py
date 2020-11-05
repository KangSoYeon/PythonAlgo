import sys 

def input_data(): 
    read = sys.stdin.readline 
    N, d, k, c = map(int,read().split()) 
    dish = [int(read()) for _ in range(N)] 
    return N, d, k, c, dish 

sol = 0  
# 입력받는 부분 
N, d, k, c, dish = input_data() 

# 여기서부터 작성
counts = [0] * (d + 1)
count = 0
for i in range(k):
    counts[dish[i]] += 1

counts[c] += 1

for i in range(1, d + 1):
    if counts[i] > 0:
        count += 1
sol = count

for i in range(k, N + k):
    counts[dish[i % N]] += 1
    if counts[dish[i % N]] == 1:
        count += 1

    counts[dish[i - k]] -= 1
    if counts[dish[i - k]] == 0:
        count -= 1

    sol = max(sol, count)

print(sol)
