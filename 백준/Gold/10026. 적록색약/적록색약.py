from collections import deque

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(matrix, x, y, visited):
    q.append([x, y])
    visited[x][y] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 이전 영역과 색이 동일하며 아직 방문한 적이 없다면,
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == matrix[r][c] and not visited[rr][cc]:
                visited[rr][cc] = 1  # 방문 기록을 남겨주고
                q.append([rr, cc])  # q에 경로를 추가해줘


N = int(input())
matrix = [list(input()) for _ in range(N)]
q = deque()

# case 1. 색약이 아닌 경우
cnt1 = 0
visited1 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(matrix, i, j, visited1)
            cnt1 += 1

# case 2. 색약인 경우; G를 R로 인식한다고 가정
# matrix 먼저 바꿔주자
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

cnt2 = 0
visited2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            bfs(matrix, i, j, visited2)
            cnt2 += 1

print(cnt1, cnt2)