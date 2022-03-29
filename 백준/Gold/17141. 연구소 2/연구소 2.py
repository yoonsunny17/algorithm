from collections import deque
from itertools import combinations

def bfs(elem):
    global aisle

    q = deque(elem)
    for k in q:
        visited[k[0]][k[1]] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] != '-' and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                aisle -= 1
                q.append([rr, cc])

    return visited[r][c] - 1


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
min_time = 987654321
# 0 : 바이러스가 퍼질 수 있는 곳
# 1 : 벽, 바이러스가 퍼질 수 없음
# 2 : 바이러스의 초기 위치가 될 수 있음

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스가 출발할 수 있는 위치들 넣어줄 list
virus = []
aisle = N*N - M # 바이러스가 지나다닐 수 있는 통로 수를 세어주자
# 벽인 부분은 헷갈리지 않도록 문자열로 바꿔주자
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = '-'
            aisle -= 1  # 벽은 통로에서 제외해줘
        if matrix[i][j] == 2:
            virus.append([i, j])

# pprint(matrix)
# print(aisle)
tmp = aisle
# virus 출발 가능한 위치에서 M개 뽑을 수 있는 경우의 수에서
for start in combinations(virus, M):
    aisle = tmp
    visited = [[0] * N for _ in range(N)]

    # q = deque(start)
    # for k in q:
    #     visited[k[0]][k[1]] = 1
    time = bfs(start)  # bfs 돌려서 최종 소요 시간 구해주자

    if time < min_time and aisle == 0:
        min_time = time

if min_time == 987654321:
    print(-1)
else:
    print(min_time)