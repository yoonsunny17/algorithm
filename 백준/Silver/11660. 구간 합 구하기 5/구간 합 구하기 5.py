import sys

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if c != 0:
            matrix[r][c] += matrix[r][c-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    cnt = 0

    for k in range(x1-1, x2):
        if y1 != 1:
            cnt -= matrix[k][y1-2]
        cnt += matrix[k][y2-1]

    print(cnt)