def dfs(node, depth):
    global flag

    visited[node] = True
    if depth == 4:
        flag = True
        return
    
    for i in arr[node]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False


n, m = map(int, input().split())
visited = [False] * n
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

flag = False
for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if flag:
        break

print(1) if flag is True else print(0)