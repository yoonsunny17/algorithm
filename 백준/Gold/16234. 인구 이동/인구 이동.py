import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append([r, c])
    temp = []  # 국경 연결되어 있는 나라들 좌표값 넣을 리스트
    temp.append([r, c])

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 아직 방문한 적이 없으면,
            if 0 <= rr < N and 0 <= cc < N and visited[rr][cc] == 0:
                # 근데 국경선 공유하고 있는 두 나라의 인구 수 차이가 L 이상 R 이하를 만족한다면
                if L <= abs(matrix[r][c] - matrix[rr][cc]) <= R:
                    # 방문처리 해주고, 다음 탐색지점으로 넘겨주고,
                    # 국경 연결되어있는 나라에 추가해줘!!
                    visited[rr][cc] = 1
                    q.append([rr, cc])
                    temp.append([rr, cc])
    
    # 더이상 bfs 돌릴 수 없으면 연결된 나라들 담긴 temp 반환해줘
    return temp

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0  # 몇번 이동해주었는지 세어 줄 변수

while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0 # 국경선 열려 있는지 확인 (1이면 열림 => 인구이동 시작)
    for i in range(N):
        for j in range(N):
            # 아직 방문한 적이 없다면, 방문처리 하고 bfs 돌리기
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 연결되어 있는 나라들 좌표 리스트 = country
                country = bfs(i, j)
                # 만약에 연결 된 나라가 2개 이상이면
                if len(country) > 1:
                    # 연합 나라 인구 이동 시켜주기
                    flag = 1
                    numb = sum(matrix[x][y] for x, y in country) // len(country)
                    for x, y in country:
                        matrix[x][y] = numb
    # 연합 해제하고 국경선 닫아주자
    # flag가 0이라면 => 더이상 인구이동이 일어나지 않음
    if not flag:
        break
    # while문 한 번 돌 때마다 (인구이동 한 번 일어날 때마다 1일씩 더하기)
    cnt += 1

print(cnt)