def dfs(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return

    else:
        for j in range(start, N):
            if numbs[j] not in stack:
                stack.append(numbs[j])
                dfs(j+1)
                stack.pop()

N, M = map(int, input().split())
numbs = list(map(int, input().split()))
numbs.sort()
stack = []
dfs(0)