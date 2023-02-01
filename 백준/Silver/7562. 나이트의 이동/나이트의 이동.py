from collections import deque

T = int(input())
for tc in range(1, T+1):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    now_x, now_y = map(int, input().split())
    final_x, final_y = map(int, input().split())

    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    q = deque()
    q.append([now_x, now_y])
    visited[now_x][now_y] = 1

    while q:
        r, c = q.popleft()

        if r == final_x and c == final_y:
            print(visited[r][c]-1)
            break

        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < l and 0 <= cc < l and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])