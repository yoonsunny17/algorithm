from collections import deque


def melt_ice():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                return False
    return True


def cnt_zero(r, c):
    cnt = 0
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc]:
            cnt += 1
    return cnt


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and new_matrix[rr][cc] and not visited[rr][cc]:
                visited[rr][cc] = 1
                new_matrix[rr][cc] = 0
                q.append([rr, cc])


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


time = 0

while True:
    time += 1
    if melt_ice():
        print(0)
        break

    # 빙산 주변 0 개수만큼 빙산 녹여주면서 갱신해줄 matrix
    new_matrix = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                zero = cnt_zero(i, j)
                new = matrix[i][j] - zero
                new_matrix[i][j] = (new if new >= 0 else 0)  # 음수면 0 처리해줘!

    matrix = [row[:] for row in new_matrix]

    rlt = 0
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] != 0:
                bfs(i, j)
                rlt += 1

    if rlt >= 2:
        print(time)
        break