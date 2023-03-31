def dfs(cnt, idx):
    if cnt == L:
        v, c = 0, 0
        for i in range(len(stack)):
            if stack[i] not in vowels:
                c += 1
            else:
                v += 1
        
        if v >= 1 and c >= 2:
            print("".join(stack))
        return
    
    for i in range(idx, C):
        if words[i] not in stack:
            stack.append(words[i])
            dfs(cnt+1, i+1)
            stack.pop()

L, C = map(int, input().split())
words = sorted(list(map(str, input().split())))

vowels = ['a', 'e', 'i', 'o', 'u']
stack = []

dfs(0, 0)