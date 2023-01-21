def dfs(i):
    if i == m:
        print(' '.join(map(str, stack)))
        return
    else:
        for j in range(1, n+1):
            if len(stack) == 0:
                stack.append(j)
                dfs(i+1)
                stack.pop()
            elif len(stack) != 0 and j >= stack[-1]:
                stack.append(j)
                dfs(i+1)
                stack.pop()

n, m = map(int, input().split())
stack = []

dfs(0)