n, m = map(int, input().split())

ans = n * m
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    temp = board[i][0]
    ans += temp
    for j in range(1, m):
        if board[i][j] > temp:
            ans += board[i][j] - temp
            temp = board[i][j]
        else:
            temp = board[i][j]

for j in range(m):
    temp = board[0][j]
    ans += temp
    for i in range(1, n):
        if board[i][j] > temp:
            ans += board[i][j] - temp
            temp = board[i][j]
        else:
            temp = board[i][j]

print(ans*2)