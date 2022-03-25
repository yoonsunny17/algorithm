def dfs(i, N, M):
    if i == M:
        print(' '.join(map(str, stack)))
    else:
        for j in range(1, N+1):
            if j not in stack:
                stack.append(j)
                dfs(i+1, N, M)
                stack.pop()

N, M = map(int, input().split())
stack = []

dfs(0, N, M)