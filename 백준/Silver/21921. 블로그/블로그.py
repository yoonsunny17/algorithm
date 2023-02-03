N, X = map(int, input().split())
numbs = list(map(int, input().split()))

if max(numbs) == 0:
    print('SAD')

else:
    max_visit = sum(numbs[:X])
    visitors = max_visit
    cnt = 1

    for i in range(X, N):
        visitors -= numbs[i-X]
        visitors += numbs[i]

        if visitors > max_visit:
            max_visit = visitors
            cnt = 1

        elif visitors == max_visit:
            cnt += 1
    
    print(max_visit)
    print(cnt)
