def dfs(v, rlt):
    rlt += 1
    visited[v] = 1

    if v == b:
        arr.append(rlt)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, rlt)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
arr = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)

print(arr[0]-1 if len(arr) > 0 else -1)