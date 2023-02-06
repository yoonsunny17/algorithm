n, m = map(int, input().split())
board1 = [list(map(int, input().split())) for _ in range(n)]
board2 = [list(map(int, input().split())) for _ in range(n)]

for row in range(n):
    for col in range(m):
        print(board1[row][col] + board2[row][col], end=' ')
    print()