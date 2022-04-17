N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

matrix.sort(key=lambda x:(x[1], x[0]))

for lst in matrix:
    print(f'{lst[0]} {lst[1]}')
