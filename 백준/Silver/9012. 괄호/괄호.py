T = int(input())
for tc in range(1, T+1):
    vps = list(input())
    rlt = 'YES'

    open_stack = []
    for v in vps:
        if v == '(':
            open_stack.append(v)
        else:
            if not len(open_stack):
                rlt = 'NO'
                break
            else:
                open_stack.pop()
                
    if len(open_stack) >= 1:
        rlt = 'NO'

    print(f'{rlt}')