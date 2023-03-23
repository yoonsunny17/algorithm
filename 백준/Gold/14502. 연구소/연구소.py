from collections import deque

def setting_walls(cnt):
    # 만약에 벽 세개 다 세웠다면 bfs 돌리자
    if cnt == 3:
        bfs()
        return
    # 아직 벽을 다 세우지 못했으면 벽 세우자 (백트래킹으로)
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                setting_walls(cnt+1)
                matrix[i][j] = 0

def bfs():
    global max_rlt

    q = deque()
    # 바이러스 위치들을 모두 큐에 넣어주자
    # deep copy 해서 쓰자
    new_matrix = [row[:] for row in matrix]
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] == 2:
                q.append([i, j])
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 안전 영역이라면,
            if 0 <= rr < N and 0 <= cc < M and not new_matrix[rr][cc]:
                # 일단 바이러스 퍼트리고, 다음 탐색지점 넘겨주자
                new_matrix[rr][cc] = 2
                q.append([rr, cc])

    rlt = 0  # 일단 안전영역 몇 개인지 세어줄 변수
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] == 0:
                rlt += 1
    
    max_rlt = max(rlt, max_rlt)

# 0 빈칸, 1 벽, 2 바이러스
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# delta 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

max_rlt = 0  # 최대 안전영역 출력할 변수
setting_walls(0)

print(max_rlt)