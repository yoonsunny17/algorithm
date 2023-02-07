from collections import deque
from pprint import pprint

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


# 공기 청정기 위치 찾기 (항상 1열)
for i in range(R):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산 함수 diffuse
def diffuse():
    # delta
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    checked = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            # 0 보다 크다면 미세먼지 있는거임!
            if graph[r][c] > 0:
                dust = 0
                for i in range(4):
                    rr = r + dr[i]
                    cc = c + dc[i]
                    # 인접한 지점이 범위 내에 존재하고, -1이 아니라면,
                    if 0 <= rr < R and 0 <= cc < C and graph[rr][cc] != -1:
                        # 먼지 확산되겠지
                        checked[rr][cc] += graph[r][c] // 5
                        dust += graph[r][c] // 5
                # 확산된 방향만큼 빼줘야 함
                graph[r][c] -= dust
    
    for i in range(R):
        for j in range(C):
            graph[i][j] += checked[i][j]

# 위쪽 공기 청정기 함수 clean_up
def clean_up():
    # up delta 우 상 좌 하
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    r, c, i = up, 1, 0  # up은 맨 처음에 공기청정기 위쪽 인덱스 찾은거 // c는 우 = 1 부터
    prev = 0

    while True:
        # 일단 쭉 가면서 봐야함
        rr = r + dr[i]
        cc = c + dc[i]
        
        # 만약에 공기청정기가 있는 곳이면, 끝!
        if r == up and c == 0:
            break
        
        # 만약 한칸씩 이동한 지점이 범위 밖이라면 인덱스 늘리고 다시 시작
        if not 0 <= rr < R or not 0 <= cc < C:
            i += 1
            continue

        # 아니라면 바람 방향대로 먼지 한칸씩 이동해주고
        graph[r][c], prev = prev, graph[r][c]
        r, c = rr, cc


# 아래쪽 공기 청정기 함수 clean_down
def clean_down():
    # down delta 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c, i = down, 1, 0
    prev = 0
    
    while True:
        rr = r + dr[i]
        cc = c + dc[i]

        # 공기청정기 있는 곳이라면 끝
        if r == down and c == 0:
            break

        # 만약 한칸씩 이동한 지점이 범위를 벗어난다면 인덱스 더해주고 다시 시작
        if not 0 <= rr < R or not 0 <= cc < C:
            i += 1
            continue

        # 그게 아니면 바람 방향대로 먼지 이동시키고 다음 먼지 방향 탐색
        graph[r][c], prev = prev, graph[r][c]
        r, c = rr, cc

# 주어진 시간 T초동안 반복할거야
for _ in range(T):
    # 일단 미세먼지 확산되겠지
    diffuse()
    clean_up()
    clean_down()

# pprint(graph)
# 공기청정기 -2 상쇄 해야 하니까 +2 해주기
print(sum(map(sum, graph)) + 2)