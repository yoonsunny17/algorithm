def dfs(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(start, N+1):
            if i not in stack:
                stack.append(i)
                dfs(i+1)
                stack.pop()

N, M = map(int, input().split())
stack = []
dfs(1)