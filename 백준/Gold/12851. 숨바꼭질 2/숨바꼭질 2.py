from collections import deque

n, k = map(int, input().split())
maxv = 100001
q = deque()
visited = [-1] * maxv
q.append(n)
visited[n] = 0

cnt = 0
while q:
    x = q.popleft()

    if x == k:
        cnt += 1
    
    for dx in [x-1, x+1, 2*x]:
        if 0 <= dx < maxv:
            if visited[dx] == -1 or visited[dx] == visited[x] + 1:
                visited[dx] = visited[x] + 1
                q.append(dx)

print(visited[k])
print(cnt)