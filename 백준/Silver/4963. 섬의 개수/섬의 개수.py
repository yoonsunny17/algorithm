import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    matrix[r][c] = 0
    dr = [0, 0, -1, 1, 1, 1, -1, -1]
    dc = [-1, 1, 0, 0, -1, 1, 1, -1]

    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < h and 0 <= cc < w and matrix[rr][cc] == 1:
            matrix[rr][cc] = 0
            dfs(rr, cc)

while True:
    w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    if w == 0 and h == 0:
        break

    print(cnt)