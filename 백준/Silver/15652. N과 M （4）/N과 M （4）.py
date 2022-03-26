def dfs(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in range(start, N+1):
            stack.append(i)
            dfs(i)
            stack.pop()


N, M = map(int, input().split())
stack = []
dfs(1)