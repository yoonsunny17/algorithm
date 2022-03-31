from collections import deque
from itertools import combinations

def bfs(elem):
    global time
    q = deque(elem)
    for k in q:
        visited[k[0]][k[1]] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] != 1 and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                if matrix[rr][cc] == 0:
                    time = max(time, visited[rr][cc])
                q.append([rr, cc])

    if list(sum(visited, [])).count(0) == list(sum(matrix, [])).count(1):
        rlt.append(time)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

virus = []
rlt = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            virus.append([i, j])

for start in combinations(virus, M):
    time = 0
    visited = [[0]*N for _ in range(N)]
    bfs(start)

if len(rlt) and min(rlt) == 0:
    print(0)
elif len(rlt) and min(rlt) > 0:
    print(min(rlt)-1)
else:
    print(-1)