n, m, r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
arr = list(map(int, input().split()))

# delta 동 1, 서 2, 북 3, 남 4
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# dice 처음에는 모든 면이 0이다 (주어진 전개도 순서상으로 주사위 번호 받을 것)
# 순서대로 위, 북, 동, 서, 남, 아래
# dice[5]가 밑면임
dice = [0, 0, 0, 0, 0, 0]

# 명령의 횟수만큼 반복해줘
for i in range(k):
    # 이동할 방향에 따라, 다음 이동할 방향을 구해줘
    move = arr[i] - 1
    rr = r + dr[move]
    cc = c + dc[move]

    # 조건4. 이동 범위 벗어나는 경우 이동하지 말고, 출력도 하지 말 것
    if not 0 <= rr < n or not 0 <= cc < m:
        continue

    # 조건2. 명령에 따라, 각 방향으로 움직일 때마다 주사위 면의 위치들이 바뀔거야
    # 0, 1, 2, 3 = 동, 서, 북, 남
    if move == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif move == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif move == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    # 조건3-1. 이동한 칸의 숫자가 0인 경우
    if board[rr][cc] == 0:
        board[rr][cc] = dice[5]
    # 조건3-2. 이동한 칸의 숫자가 0이 아닌 경우
    else:
        dice[5] = board[rr][cc]
        board[rr][cc] = 0

    # 움직인 칸 = 원래 내 위치로 초기화
    r, c = rr, cc

    print(dice[0])