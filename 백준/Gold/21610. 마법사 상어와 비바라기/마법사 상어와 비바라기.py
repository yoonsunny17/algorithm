'''
1. 구름 이동
이동 + 비 내리기 동시에 구현
맵을 벗어나면 핸들링이 필요함
이동한 구름의 좌표가 필요하기 때문에 큐에 담아주기
추후에 이동한 구름의 자리에 또다시 구름이 생기면 안되므로 visited 체크 리스트 만들어서 갱신해주기

2. 물 복사
구름이 사라진 것 + 물 복사 되는 것 같이 구현
큐에 넣었던 좌표 하나씩 꺼내 대각선만 체크하기
범위 안이면서 + 물이 존재한다면 ==> 현재 자리에서 물을 +1 해주기

3. 구름 생성
전체 바구니를 검사해서 구름을 생성해야 하므로, 아까 만든 visited와 물이 2이상인 지점을 다시 큐에 넣기

4. 모든 물의 양 구하기
N*N 바구니를 모두 더해 답 출력하기
'''

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for  _ in range(M)]

# 주어진 8개의 방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 비바라기 시전했을 때 비구름이 생기는 위치
clouds = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])

# 1. 구름 이동 후 비 내리기 함수
def move_rain(d, s):
    size = len(clouds)
    for _ in range(size):
        r, c = clouds.popleft()
        # 이어진 격자: 배열이 이어져 있다는 것 주의!
        rr = (r + dr[d] * s) % N
        cc = (c + dc[d] * s) % N
        # 이동한 다음 구름 위치 저장해주고
        clouds.append([rr, cc])
        # 구름 사라진 위치 표시해주고
        visited[rr][cc] = True
        # 물 +1 해줘
        matrix[rr][cc] += 1


# 2. 물 복사
def water_dup():
    while clouds:
        # 대각선 검사 (idx 1, 3, 5, 7만 확인하면 됨)
        r, c = clouds.popleft()
        for i in range(1, 8, 2):
            rr = r + dr[i]
            cc = c + dc[i]
            # 만약 대각선 위치가 범위 내에 존재하고, 0 보다 크다면, +1 해줘
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] > 0:
                matrix[r][c] += 1


for d, s in moves:
    visited = [[False] * N for _ in range(N)]
    # 1. 구름 이동 후 비 내리기 (idx 생각해서 d-1 넣어주기!)
    move_rain(d-1, s)
    # 2. 물 복사
    water_dup()
    # 3. 구름 생성
    for i in range(N):
        for j in range(N):
            # 물의 양이 2 이상이고, 구름이 있던 곳이 아니라면
            if matrix[i][j] >= 2 and not visited[i][j]:
                # 구름 생성해주고, 물 -2 해줘
                clouds.append([i, j])
                matrix[i][j] -= 2

answer = 0
for i in range(N):
    for j in range(N):
        answer += matrix[i][j]
print(answer)
