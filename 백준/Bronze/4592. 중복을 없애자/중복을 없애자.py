while True:
    ans = []
    numbs = input().split()
    if numbs[0] == '0':
        break
    numbs.remove(numbs[0])

    for numb in numbs:
        if len(ans) == 0:
            ans.append(numb)
        elif ans[-1] != numb:
            ans.append(numb)
    ans.append('$')

    print(*ans)