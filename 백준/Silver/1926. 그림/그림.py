from collections import deque
from pprint import pprint

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    width = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < n and 0 <= cc < m:
                if matrix[rr][cc] == 1 and not visited[rr][cc]:
                    visited[rr][cc] = visited[r][c] + 1
                    width += 1
                    q.append([rr, cc])
    return width

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0
max_width = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            max_width = max(max_width, bfs(i, j))
            cnt += 1

print(cnt)
print(max_width)