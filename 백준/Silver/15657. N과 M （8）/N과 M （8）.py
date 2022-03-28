def dfs(i):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in range(i, len(numbs)):
            stack.append(numbs[i])
            dfs(i)
            stack.pop()


N, M = map(int, input().split())
numbs = list(map(int, input().split()))
numbs.sort()
stack = []
dfs(0)