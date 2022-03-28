from pprint import pprint

def f(r, c, N):
    global plus, minus, zero

    numb = matrix[r][c]

    for i in range(r, r+N):
        for j in range(c, c+N):
            if matrix[i][j] != numb:
                f(r, c, N//3)
                f(r, c+N//3, N//3)
                f(r, c+(N//3)*2, N//3)
                f(r+N//3, c, N//3)
                f(r+N//3, c+N//3, N//3)
                f(r+N//3, c+(N//3)*2, N//3)
                f(r+(N//3)*2, c, N//3)
                f(r+(N//3)*2, c+N//3, N//3)
                f(r+(N//3)*2, c+(N//3)*2, N//3)
                return

    if numb == 1:
        plus += 1
    elif numb == -1:
        minus += 1
    else:
        zero += 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
plus = minus = zero = 0
f(0, 0, N)
print(f'{minus}\n{zero}\n{plus}')