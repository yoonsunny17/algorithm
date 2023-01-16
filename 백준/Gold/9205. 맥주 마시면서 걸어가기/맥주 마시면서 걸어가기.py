from collections import deque

def bfs():
    q = deque()
    q.append([home_x, home_y])

    while q:
        x, y = q.popleft()
        if abs(fes_x-x) + abs(fes_y-y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                xx, yy = arr[i]
                if abs(x-xx) + abs(y-yy) <= 1000:
                    visited[i] = 1
                    q.append([xx, yy])
    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    arr = []
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append([x, y])
    fes_x, fes_y = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()