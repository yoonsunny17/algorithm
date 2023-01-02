from collections import deque

M, N, H = map(int, input().split())
matrix = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]
visited = [list([0] * M for _ in range(N)) for _ in range(H)]

day = 0

# 상 하 좌 우 앞 뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

q = deque()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if matrix[k][j][i] == 1:
                q.append([k, j, i])

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            zz = z + dz[i]
            yy = y + dy[i]
            xx = x + dx[i]
            # 범위 내애 존재하고, 아직 익지 않은 토마토인 경우(= 0)
            if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and matrix[zz][yy][xx] == 0:
                matrix[zz][yy][xx] = matrix[z][y][x] + 1
                q.append([zz, yy, xx])

    return matrix

bfs()

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
            else:
                day = max(day, c)

print(day-1)