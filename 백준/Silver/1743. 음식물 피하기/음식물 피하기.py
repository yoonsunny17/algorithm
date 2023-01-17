from collections import deque

def bfs(matrix, r, c):
    q = deque()
    q.append([r, c])
    matrix[r][c] = 0
    cnt = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 < rr <= N and 0 < cc <= M and matrix[rr][cc] == 1:
                q.append([rr, cc])
                matrix[rr][cc] = 0
                cnt += 1
    
    return cnt

N, M, K = map(int, input().split())
matrix = [[0]*(M+1) for _ in range(N+1)]
rlt = 0
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r][c] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(1, N+1):
    for j in range(1, M+1):
        if matrix[i][j] == 1:
            ans = bfs(matrix, i, j)

            rlt = max(rlt, ans)

print(rlt)