import bisect

N = int(input())
pos = [int(input()) for _ in range(N)]

pos.sort()
answer = 0
#bisect 이용하면
for i in range(N-2):
    for j in range(i+1, N-1):
        gap = pos[j] - pos[i]

        a = bisect.bisect_left(pos, pos[j] + gap)
        b = bisect.bisect_right(pos, pos[j] + (gap*2))

        answer += (b - a)

print(answer)

