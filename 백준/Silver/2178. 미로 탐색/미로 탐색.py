from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] == 1 and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                if rr == N-1 and cc == M-1:
                    return visited[rr][cc]
                q.append([rr, cc])

rlt = bfs()
print(rlt)
