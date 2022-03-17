from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    water_q = deque()
    cute_q = deque()
    cute_q.append(cute)
    for i in range(len(water)):
        water_q.append(water[i])

    while True:
        if not cute_q:
            break

        for _ in range(len(water_q)):
            r, c = water_q.popleft()
            for i in range(4):
                wr = r + dr[i]
                wc = c + dc[i]
                if 0 <= wr < R and 0 <= wc < C and matrix[wr][wc] == '.':
                    water_q.append([wr, wc])
                    matrix[wr][wc] = '*'

        for _ in range(len(cute_q)):
            x, y = cute_q.popleft()
            for i in range(4):
                cr = x + dr[i]
                cc = y + dc[i]
                if 0 <= cr < R and 0 <= cc < C:
                    if matrix[cr][cc] == '.' and not visited[cr][cc]:
                        cute_q.append([cr, cc])
                        visited[cr][cc] = visited[x][y] + 1
                    if matrix[cr][cc] == 'D':
                        return visited[x][y]

    return 'KAKTUS'


R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
water = []
cute = []

for i in range(R):
    for j in range(C):
        if matrix[i][j] == '*':
            water.append([i, j])
        if matrix[i][j] == 'S':
            cute.extend([i, j])
            matrix[i][j] = '.'
            visited[i][j] = 1

print(bfs())