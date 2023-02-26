import sys

# ㅗ 모양 제외 다른 모양들 최댓값 계산하기
def dfs(r, c, dsum, cnt):
    global maxV
    # 모양 완성되었을 때 최댓값 계산해주기
    if cnt == 4:
        maxV = max(maxV, dsum)
        return
    
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        # 탐색 지점이 범위 내에 존재하고, 아직 방문하지 않았다면,
        if 0 <= rr < N and 0 <= cc <M and not visited[rr][cc]:
            # 방문 표시하고, dfs 재귀 돌리고, 방문표시 해제해줭
            visited[rr][cc] = True
            dfs(rr, cc, dsum + matrix[rr][cc], cnt+1)
            visited[rr][cc] = False


# ㅗ 모양 최댓값 계산하기
def cross(r, c):
    global maxV

    for i in range(4):
        # 초기값은 시작지점의 값으로 지정
        temp = matrix[r][c]
        # 세 방향씩 검사해야 하니까 뺑뺑이
        for k in range(3):
            t = (i+k) % 4
            rr = r + dr[t]
            cc = c + dc[t]
            # 탐색 지점이 범위 내에 존재하지 않는 경우,
            if not (0 <= rr < N and 0 <= cc < M):
                # temp값을 초기화 해주고 끝내
                temp = 0
                break
            # 종료 조건에 걸리지 않는 경우면 temp값 누적
            temp += matrix[rr][cc]
        maxV = max(maxV, temp)
    

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 상 하 좌 우 delta
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

maxV = 0 # 최댓값 변수

for i in range(N):
    for j in range(M):
        # 방문처리 해주고; dfs 돌리고; 방문처리 해재하고; ㅗ모양 확인
        visited[i][j] = True
        dfs(i, j, matrix[i][j], 1)
        visited[i][j] = False
        cross(i, j)

print(maxV)