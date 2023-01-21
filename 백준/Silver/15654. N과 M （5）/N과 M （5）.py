def dfs(i):
    if i == m:
        print(' '.join(map(str, stack)))
        return
    
    else:
        for numb in numbs:
            if numb not in stack:
                stack.append(numb)
                dfs(i+1)
                stack.pop()

n, m = map(int, input().split())
numbs = list(map(int, input().split()))
numbs.sort()
stack = []

dfs(0)