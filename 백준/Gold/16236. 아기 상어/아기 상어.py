from collections import deque

def bfs(row, col):
    global fish
    fish = []
    q = deque()
    q.append([row, col, 0])
    visited = [[0]*N for _ in range(N)]
    visited[row][col] = 1

    while q:
        r, c, d = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                if 0 <= matrix[rr][cc] <= shark_size:
                    visited[rr][cc] = 1
                    q.append([rr, cc, d+1])
                    if 0 < matrix[rr][cc] < shark_size:
                        fish.append([rr, cc, d+1])


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

start_x, start_y = 0, 0
shark_size = 2

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start_x = i
            start_y = j
matrix[start_x][start_y] = 0
eat, time = 0, 0
fish = []


while True:
    bfs(start_x, start_y)
    if not len(fish):
        print(time)
        exit()

    else:
        fish.sort(key=lambda x:(x[2], x[0], x[1]))
        matrix[fish[0][0]][fish[0][1]] = 0
        eat += 1
        time += fish[0][2]
        start_x = fish[0][0]
        start_y = fish[0][1]
        
        if eat == shark_size:
            shark_size += 1
            eat = 0
