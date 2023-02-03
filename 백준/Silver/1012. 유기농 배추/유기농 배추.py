import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc]:
            matrix[rr][cc] -= 1
            dfs(rr, cc)



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)