n, m = map(int, input().split())
board = [input() for _ in range(n)]
cnt = []

for i in range(n-7):
    for j in range(m-7):
        idx1, idx2 = 0, 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'W':
                        idx1 += 1
                    else: idx2 += 1
                
                else:
                    if board[x][y] != 'B':
                        idx1 += 1
                    else: idx2 += 1
        
        cnt.append(min(idx1, idx2))

print(min(cnt))