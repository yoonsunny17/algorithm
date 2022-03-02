N = int(input())
codes = [input() for i in range(N)]
stack = [] # empty stack
for code in codes:
    if code == 'pop':
        if not len(stack): print(-1)
        else: print(stack.pop())
    elif code == 'size':
        print(len(stack))
    elif code == 'empty':
        if not len(stack): print(1)
        else: print(0)
    elif code == 'top':
        if not len(stack): print(-1)
        else: print(stack[-1])
    else:
        stack.append(code[5:])