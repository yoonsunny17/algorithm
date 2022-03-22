def dfs(start):
    visited[start] = 1
    global cnt
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            cnt += 1

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
dfs(start=1)
print(cnt)