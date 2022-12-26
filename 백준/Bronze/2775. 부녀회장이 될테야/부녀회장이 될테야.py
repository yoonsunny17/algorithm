T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    numbs = [x for x in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            numbs[j] += numbs[j-1]
    
    print(numbs[-1])