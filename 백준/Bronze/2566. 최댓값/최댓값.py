matrix = [list(map(int, input().split())) for _ in range(9)]

max_numb = 0
max_r, max_c = 0, 0

for i in range(9):
    for j in range(9):
        if max_numb <= matrix[i][j]:
            max_r = i + 1
            max_c = j + 1
            max_numb = matrix[i][j]

print(f"{max_numb}\n{max_r} {max_c}")