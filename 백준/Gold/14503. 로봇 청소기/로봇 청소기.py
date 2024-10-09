import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

matrix[r][c] = 2 # 초기 위치 청소해줘
cleaning = 1 # 총 얼마나 청소했는지 출력할 변수. 초기위치 청소했으니 1 넣고 시작

while True:
    flag = False # 청소할 구역이 남아있지 않은 경우를 False로 설정

    # 반시계 방향으로 탐색할 것
    for _ in range(4):
        d = (d + 3) % 4
        rr = r + dr[d]
        cc = c + dc[d]
        # 탐색할 구역이 범위 내에 존재하고, 아직 청소한 적이 없으면 청소해줘
        if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] == 0:
            # 청소했다고 표시하고, 같은 방향으로 탐색 이어가고, flag = True 갱신해줘
            matrix[rr][cc] = 2
            cleaning += 1
            r, c = r + dr[d], c + dc[d]
            flag = True
            break
    
    # 더이상 청소할 구역이 남지 않은 경우
    if not flag:
        # 후진하려고 보니 벽인 경우라면 그대로 종료해줘
        if matrix[r-dr[d]][c-dc[d]] == 1:
            print(cleaning)
            break
        # 후진이 가능한 경우(청소는 되어있는 경우), 한 칸 후진해줘
        else:
            r, c = r - dr[d], c - dc[d]
