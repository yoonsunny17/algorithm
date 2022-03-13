from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 상 하 좌 우 탐색하기 위한 델타 표현해주기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    # empty queue 생성 및 start 지점 넣어주기
    queue = deque()
    queue.append([0,0])
    # 몇 번 (몇 시간) 후에 완전히 녹았는지 체크해 줄 변수 초기화
    cnt = 0
    # 방문기록 남겨줄 이차원 리스트 만들어주기
    visited = [[0] * C for _ in range(R)]
    # 시작지점 방문 기록 남겨주자
    visited[0][0] = 1

    # queue가 비어있을 때까지 반복해
    while queue:
        # queue에서 r, c를 꺼내줘 (선입선출로)
        r, c = queue.popleft()
        # delta의 네방향을 탐색할거야
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # rr과 cc가 범위 내에 있고, 방문 기록이 아직 존재하지 않을 때,
            if 0 <= rr < R and 0 <= cc < C and visited[rr][cc] == 0:
                # 근데 치즈가 아닌 부분이라면,
                if matrix[rr][cc] == 0:
                    # 방문 기록을 남겨줘
                    visited[rr][cc] = 1
                    # 내가 지나온 길을 알려줘야 하니까 queue에도 넣어줘
                    queue.append([rr, cc])
                # 만약 치즈가 있는 부분이라면 (1인 부분이라면):
                elif matrix[rr][cc] == 1:
                    # 녹게 만들어주고 (0으로 바꿔주고)
                    matrix[rr][cc] = 0
                    # cnt += 1 해주고
                    cnt += 1
                    # 방문 기록을 남겨줘, 단!! queue에는 남기면 안돼! queue에 넣게 되면 치즈 안쪽까지 녹아버려
                    visited[rr][cc] = 1

    # cnt = 매 시간마다 녹이는 테두리의 치즈 수
    last.append(cnt)
    return cnt

# 첫 시간도 포함되므로 -1 해주기
time = -1
last = []

while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break

print(f'{time}\n{last[-2]}')