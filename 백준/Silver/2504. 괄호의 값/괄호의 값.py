strings = list(input())
stack = []
ans = 0
cnt = 1

for i in range(len(strings)):
    if strings[i] == "(":
        stack.append(strings[i])
        cnt *= 2
    
    elif strings[i] == "[":
        stack.append(strings[i])
        cnt *= 3
    
    elif strings[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if strings[i-1] == "(":
            ans += cnt
        stack.pop()
        cnt //= 2
    
    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if strings[i-1] == "[":
            ans += cnt
        stack.pop()
        cnt //= 3

if stack:
    print(0)
else:
    print(f'{ans}')