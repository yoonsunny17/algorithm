def f(r, c, N):
    global white, blue
    color = matrix[r][c]
    for i in range(r, r+N):
        for j in range(c, c+N):
            if matrix[i][j] != color:
                f(r, c, N//2)
                f(r, c+N//2, N//2)
                f(r+N//2, c, N//2)
                f(r+N//2, c+N//2, N//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0

f(0, 0, N)
print(white)
print(blue)