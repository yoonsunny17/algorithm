def dfs():
    if len(stack) == n:
        print(' '.join(map(str, stack)))
        return
    
    else:
        for numb in numbs:
            if numb not in stack:
                stack.append(numb)
                dfs()
                stack.pop()

n = int(input())
numbs = [x for x in range(1, n+1)]
stack = []
dfs()