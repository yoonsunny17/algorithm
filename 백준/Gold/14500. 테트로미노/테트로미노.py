# 가운데 손가락 모양 제외 네가지 테트리스 dfs 돌리기 함수
def tetris(r, c, idx, cnt):
    global max_cnt

    # 테트리스 블록 네개를 다 모았다면,
    if idx == 4:
        # 최댓값 갱신 해줘
        if max_cnt < cnt:
            max_cnt = max(max_cnt, cnt)

    # 아직 다 모으지 않았다면, 열심히 모아
    else:
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 아직 탐색한 적이 없으면
            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc]:
                # 방문 기록 남기고 다음번 블럭 탐색하러 가봐
                visited[rr][cc] = 1
                tetris(rr, cc, idx+1, cnt+matrix[rr][cc])
                # 백트래킹!
                visited[rr][cc] = 0


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# delta 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

max_cnt, max_rlt = 0, 0
min_cnt = float('inf')


# 가운데손가락 모양 테트리스를 배치해보자
# 우선 십자가 모양으로 배치해본다고 생각해보자 = 하나를 중심으로 잡고, 네방향 탐색해봐
# 네방향 탐색했을 때 그 중 가장 큰 세가지 숫자 + 중심 숫자 & 최댓값 갱신하면 되겠다
# 재귀함수로 불가능한 사각형
def cross(r, c):
    # 가운데 값 고정
    max_rlt = matrix[r][c]
    edges = 4  # 네방향 탐색해줄 것 (탐색지점이 아닐 때 하나씩 빼줄 예정)
    min_rlt = float('inf')

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if edges == 2:
            return 0

        # 탐색 지점을 벗어나는 경우, edge -= 1
        if rr < 0 or rr >= N or cc < 0 or cc >= M:
            edges -= 1
            continue

        max_rlt += matrix[rr][cc]
        if matrix[rr][cc] < min_rlt:
            min_rlt = matrix[rr][cc]

    if edges == 4:
        max_rlt -= min_rlt

    return max_rlt


for i in range(N):
    for j in range(M):
        # tetris function backtracking
        visited[i][j] = 1
        tetris(i, j, 1, matrix[i][j])
        visited[i][j] = 0

        temp = cross(i, j)
        if temp > max_cnt:
            max_cnt = max(temp, max_cnt)

print(max_cnt)