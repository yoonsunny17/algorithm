from collections import deque
import sys

def change_walls(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                change_walls(cnt+1)
                matrix[i][j] = 0


def bfs():
    global max_rlt
    virus = deque()

    new_matrix = [row[:] for row in matrix]
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] == 2:
                virus.append([i, j])

    while virus:
        r, c = virus.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and not new_matrix[rr][cc]:
                new_matrix[rr][cc] = 2
                virus.append([rr, cc])

    rlt = 0
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] == 0:
                rlt += 1

    max_rlt = max(max_rlt, rlt)

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_rlt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


change_walls(0)
print(max_rlt)