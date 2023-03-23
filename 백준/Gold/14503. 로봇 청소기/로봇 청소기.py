N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# delta 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1  # 몇 칸 청소했는지 세어주기

'''
1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소해줘
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우? (flag = 0; 청소해야 할 부분이 없음)
    2-1. 바라보는 방향은 유지하면서, 후진 가능하다면 한 칸 후진하고 1번으로 돌아가
    2-2. 바라보는 방향의 뒤쪽이 벽이면 그대로 끝내!
3. 현재 칸의 주변 4칸 중 청소되지 않은 칸이 있는 경우? (flag = 1; 청소해야 할 부분이 남음)
    3-1. 반시계 방향으로 90도 회전해
    3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 칸이 빈칸이면 한 칸 앞으로 가
    3-3. 1번으로 돌아가서 반복해줘
'''

while True:
    flag = 0  # 청소해야 할 부분이 안남음

    for _ in range(4):
        d = (d+3)%4  # 반시계방향으로 회전 (3-1)
        rr = r + dr[d]
        cc = c + dc[d]
        # 바라본 방향의 칸이 범위 내에 존재하고, 아직 청소한 적이 없는 부분인 경우라면,
        if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc]:
            # 그리고 아직 방문한 적도 없다면,
            if not visited[rr][cc]:
                # 방문 처리를 해주고, 청소 칸 +1, 위치 갱신해주고,
                # 하나라도 청소할 방향이 남아있으면 flag 1로 변경해줘
                visited[rr][cc] = 1
                cnt += 1
                r = rr
                c = cc
                flag = 1
                break
    # 네 방향 모두 청소할 수 없는 경우라면
    if flag == 0:
        # 만약에 후진이 가능한 경우라면, (청소되어있는 벽인 경우라면)
        if matrix[r - dr[d]][c - dc[d]] == 1:
            # (2-2) 그대로 끝내자
            print(cnt)
            break
        # 아니면 1번으로 돌아가서 반복하자
        # 반복하자 = 위치를 갱신하자
        else:
            r, c = r - dr[d], c - dc[d]