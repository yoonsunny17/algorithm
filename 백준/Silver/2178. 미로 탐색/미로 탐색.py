from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 상 하 좌 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # rr, cc 가 범위 내에 존재하고, matrix에서 1이고 아직 방문 안했으면
            if 0 <= rr < n and 0 <= cc < m and matrix[rr][cc] == 1 and not visited[rr][cc]:
                # 방문 처리 해줘 근데 누적으로
                visited[rr][cc] = visited[r][c] + 1
                # 만약에 도착지점에 도달했으면 리턴해줘
                if rr == n-1 and cc == m-1:
                    return visited[rr][cc]
                # 다음 탐색 지점 넣어줘
                q.append([rr, cc])

rlt = bfs()

print(rlt)