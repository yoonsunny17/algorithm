import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = 1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)