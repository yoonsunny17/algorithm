N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
virus = []
S, X, Y = map(int, input().split())

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            virus.append([matrix[i][j], i, j])

virus.sort()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while S:
    for _ in range(len(virus)):
        v, r, c = virus.pop(0)
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                visited[rr][cc] = v
                virus.append([v, rr, cc])

    S -= 1

print(visited[X-1][Y-1])