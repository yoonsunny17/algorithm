from collections import deque

M, N, H = map(int, input().split())

box = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

q = deque()
for k in range(H):
    for j in range(N):
        for i in range(M):
            if box[k][j][i] == 1:
                q.append([k, j, i])

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            zz = z + dz[i]
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and not box[zz][yy][xx]:
                box[zz][yy][xx] = box[z][y][x] + 1
                q.append([zz, yy, xx])

    return box

bfs()
rlt = 0

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            else:
                if k > rlt:
                    rlt = k

print(rlt - 1)