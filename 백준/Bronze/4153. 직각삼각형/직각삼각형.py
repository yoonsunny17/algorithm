while True:
    numbs = list(map(int, input().split()))
    if numbs == [0, 0, 0]:
        break
    else:
        numbs.sort()
        if numbs[0]**2 + numbs[1]**2 == numbs[2]**2:
            print('right')
        else:
            print('wrong')