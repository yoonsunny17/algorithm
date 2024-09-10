from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < n and 0 <= cc < m and maps[rr][cc] and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])
        
            if rr == n-1 and cc == m-1:
                return visited[n-1][m-1]
    
    return -1