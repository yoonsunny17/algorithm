from collections import deque

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# delta 4방향 탐색; 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()
# start 지점 찾기 = 익은 토마토 위치 찾기
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            q.append([i, j])

def bfs():
    # queue가 빌 때까지
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색했는데 범위 idx가 범위 내에 존재하고, 익지 않은 토마토라면 익혀주자
            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] == 0:
                matrix[rr][cc] = matrix[r][c] + 1
                q.append([rr, cc])

    return matrix


bfs()
rlt = 0

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

        else:
            if j > rlt:
                rlt = j

print(rlt - 1)