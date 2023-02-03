from collections import deque

def bfs(r, c, visited):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색할 지점이 범위 내에 존재하고, 아직 방문한 적 없으면서, 지금 지점이랑 같은 색이라면
            if 0 <= rr < n and 0 <= cc < n and not visited[rr][cc] and matrix[r][c] == matrix[rr][cc]:
                # 방문 처리 해주고 다음 탐색지점으로 넣어주자
                visited[rr][cc] = 1
                q.append([rr, cc])


n = int(input())
matrix = [list(input()) for _ in range(n)]

# delta
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# case1. 적록색약 아닌 경우
cnt1 = 0  # 구역 몇개인지 세어줄 변수
visited1 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, visited1)
            # bfs 빠져나왔다 = 인접 구역에 같은색 없다
            cnt1 += 1

# case2. 적록색약인 경우
# G -> R로 바꿔주고 bfs 돌려주자
cnt2 = 0  # 구역 몇개인지 세어줄 변수
visited2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, visited2)
            cnt2 += 1

print(f'{cnt1} {cnt2}')