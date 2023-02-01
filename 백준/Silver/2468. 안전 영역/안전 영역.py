from collections import deque
from pprint import pprint

def bfs(r, c, numb):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < n and 0 <= cc < n:
                if graph[rr][cc] > numb and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    q.append([rr, cc])

n = int(input())
max_num = 0
graph = []

for _ in range(n):
    low = list(map(int, input().split()))
    graph.append(low)

    for i in low:
        if i > max_num:
            max_num = i

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = []

for i in range(max_num):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if graph[r][c] > i and not visited[r][c]:
                bfs(r, c, i)
                cnt += 1

    result.append(cnt)

print(max(result))