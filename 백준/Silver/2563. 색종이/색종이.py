matrix = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] = 1

for row in matrix:
    cnt += row.count(1)

print(cnt)