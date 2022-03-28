def tree(r, c, N):
    start = matrix[r][c]

    for i in range(r, r+N):
        for j in range(c, c+N):
            if matrix[i][j] != start:
                stack.append('(')
                tree(r, c, N//2)
                tree(r, c+N//2, N//2)
                tree(r+N//2, c, N//2)
                tree(r+N//2, c+N//2, N//2)
                stack.append(')')
                return stack

    if start:
        stack.append(1)
    if start == 0:
        stack.append(0)

    return stack


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
stack = []
rlt = tree(0, 0, N)
print(''.join(map(str, rlt)))