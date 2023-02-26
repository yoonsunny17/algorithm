from collections import deque

def bfs(r, c):
    q = deque()
    q.append([r, c])
    cnt = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 만약 탐색 지점이 범위 내에 존재하고, 채워지지 않은 부분이라면
            if 0 <= rr < M and 0 <= cc < N and graph[rr][cc] == 0:
                # 그래프 채워주고, 다음 탐색지점으로 넘겨주고, 카운트 해줘
                graph[rr][cc] = 1
                q.append([rr, cc])
                cnt += 1
    return cnt

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # y (row), x (column) 받은 좌표 내에 해당하는 그래프 좌표들은 1로 채워주자
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

res = [] # 각 영역 너비 받을 리스트 초기화

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        # 만약에 그래프가 직사각형으로 채워져 있지 않으면
        if graph[i][j] == 0:
            # 채워주고 bfs 돌려주고 너비 세어주자
            graph[i][j] = 1
            res.append(bfs(i, j))

print(len(res))
print(*sorted(res))