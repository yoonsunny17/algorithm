from collections import deque

N, K = map(int, input().split())
max_numb = 100000
time = [0] * (max_numb+1)

q = deque()
q.append(N)

while q:
    x = q.popleft()
    lst = [x+1, x-1, x*2]
    if x == K:
        print(time[x])
        break
    for dx in lst:
        if 0 <= dx <= max_numb and not time[dx]:
            time[dx] = time[x] + 1
            q.append(dx)