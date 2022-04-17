N, K = map(int, input().split())
numbs = [True] * (N+1)
rlt = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if numbs[j]:
            numbs[j] = False
            rlt += 1
            if rlt == K:
                print(j)
                break