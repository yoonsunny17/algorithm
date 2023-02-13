import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

dfs(1)

for i in range(2, len(visited)):
    print(visited[i])