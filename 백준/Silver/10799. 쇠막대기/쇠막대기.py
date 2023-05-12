lazers = list(input())
ans = 0
stack = []

for i in range(len(lazers)):
    if lazers[i] == '(':
        stack.append('(')
    else:
        if lazers[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)