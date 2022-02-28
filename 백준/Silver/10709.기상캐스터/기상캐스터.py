H, W = map(int, input().split())
weather = [input() for _ in range(H)]
matrix = list([0]*W for _ in range(H))

for i in range(H):
    cloud = False
    cnt = 1
    for j in range(W):
        if not cloud and weather[i][j] == '.': # 구름이 아예 없다면
            matrix[i][j] = -1 # -1로 표시해줘
        elif weather[i][j] == 'c': # 구름이 있다면
            cloud = True
            matrix[i][j] = 0 # 구름이 있는 자리를 0으로 표시해줘
            cnt = 1
        elif cloud and weather[i][j] == '.': # 구름이 올 수 있는 자리라면
            matrix[i][j] = cnt
            cnt += 1

for i in range(H):
    for j in range(W):
        print(matrix[i][j], end=' ')
    print()