from collections import deque

def cleaning(r, c, d):
    global cnt
    
    if matrix[r][c] == 0:
        matrix[r][c] = 2
        cnt += 1
        
    for _ in range(4):
        dd = (d+3) % 4
        rr = r + dr[dd]
        cc = c + dc[dd]

        if matrix[rr][cc] == 0:
            cleaning(rr, cc, dd)
            return

        d = dd
        
    dd = (d+2) % 4
    rr = r + dr[dd]
    cc = c + dc[dd]
    if matrix[rr][cc] == 1:
        return
    else:
        cleaning(rr, cc, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
cleaning(r, c, d)

print(cnt)
