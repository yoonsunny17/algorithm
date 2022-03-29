import sys
from collections import deque

def bfs(lst_v): #바이러스1,2,3 위치
    global time
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                visited[i][j] = '-'

    for i in lst_v:
        q.append(vi_lst[i])
        r,c = vi_lst[i]
        visited[r][c] = 1

    while q:
        r,c = q.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                visited[rr][cc]= visited[r][c]+1
                q.append((rr,cc))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                break
            else:
                time = min(time, visited[r][c] - 1)
        if visited[i][j] == 0:
            time = -1
            break

    return

def dfs(m,n,lst):
    global time
    if len(lst) == m:
        time =99999
        bfs(lst)
        time_lst.append(time)
        return
    for k in range(n):
        dfs(m, k, lst+[k])

N, M = map(int,input().split())
#N크기, M은 바이러스의 수

matrix = [list(map(int,input().split())) for _ in range(N)]
vi_lst = []
dr,dc = [-1,1,0,0],[0,0,-1,1]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            vi_lst.append((i, j))
time_lst = []
dfs(M,len(vi_lst), [])

if sum(time_lst) == -len(time_lst):
    print(-1)
else:
    ans = N * N
    for item in time_lst:
        if item > -1 and ans > item:
            ans = item
    print(ans)