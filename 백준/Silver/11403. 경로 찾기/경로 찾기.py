n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()