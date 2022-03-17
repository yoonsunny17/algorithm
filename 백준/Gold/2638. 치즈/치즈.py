from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0])
    visited = [[0] * M for _ in range(N)]
    cheese = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc] and not visited[rr][cc]:
                visited[rr][cc] = 1
                q.append([rr, cc])
            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc]:

                cheese[rr][cc] += 1

    melt = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 2:
                melt += 1
                cheese[i][j] = 0
                visited[i][j] = 1
                matrix[i][j] = 0

    return melt

time = -1
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
print(time)