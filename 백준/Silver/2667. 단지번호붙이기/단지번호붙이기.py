from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(matrix, r, c):
    q = deque()
    q.append([r, c])
    matrix[r][c] = 0
    cnt = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 1:
                cnt += 1
                q.append([rr, cc])
                matrix[rr][cc] = 0
            
    return cnt

arr = [bfs(matrix, r, c) for r in range(N) for c in range(N) if matrix[r][c] == 1]
arr.sort()
print(len(arr))
for a in arr:
    print(a)