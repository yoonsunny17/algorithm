import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs1(i, j):
    global cnt
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    matrix[i][j] = cnt

    while q:
        x, y = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] == 1 and not visited[xx][yy]:
                q.append([xx, yy])
                matrix[xx][yy] = cnt
                visited[xx][yy] = 1

def bfs2(w):
    global answer
    bridge = [[-1]*N for _ in range(N)]  # 다리의 거리를 저장해 줄 배열
    q = deque()

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == w:
                q.append([i, j])
                bridge[i][j] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < N:
                if matrix[xx][yy] > 0 and matrix[xx][yy] != w:
                    answer = min(answer, bridge[x][y])

                if matrix[xx][yy] == 0 and bridge[xx][yy] == -1:
                    bridge[xx][yy] = bridge[x][y] + 1
                    q.append([xx, yy])


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 1  # 섬 번호 붙여줄거임
answer = sys.maxsize

for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j]:
            bfs1(i, j)
            cnt += 1


for i in range(1, cnt):
    bfs2(i)

print(answer)
