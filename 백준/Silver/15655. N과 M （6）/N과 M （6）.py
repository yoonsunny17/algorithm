def dfs(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in range(start, N):
            if numbs[i] not in stack:
                stack.append(numbs[i])
                dfs(i+1)
                stack.pop()


N, M = map(int, input().split())
numbs = list(map(int, input().split()))
numbs.sort()
stack = []
dfs(0)