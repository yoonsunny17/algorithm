N, H = map(int, input().split())

data = []

barrier = [0] * (H + 1)
down = [0] * (H+1)
up = [0] * (H+1)

for _ in range(N):
    data.append(int(input()))

cnt = 0
for i in data:
    if cnt % 2 == 0:
        cnt += 1
        up[i] += 1
    else:
        cnt += 1
        down[H - i + 1] += 1

for i in range(H - 1, 0, -1):
    up[i] += up[i + 1]

for j in range(1, H + 1):
    down[j] += down[j - 1]

for k in range(1, H + 1):
    barrier[k] = up[k] + down[k]

print(min(barrier[1:]), barrier[1:].count(min(barrier[1:])))