def dfs(idx, n, m):
    if idx == m:
        print(' '.join(map(str, stack)))
        return

    else:
        for i in range(1, n+1):
            stack.append(i)
            dfs(idx+1, n, m)
            stack.pop()

n, m = map(int, input().split())
stack = []
dfs(0, n, m)