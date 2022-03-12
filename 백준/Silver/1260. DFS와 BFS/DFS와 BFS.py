import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)

def bfs(V):

    queue = [V]
    visited[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)