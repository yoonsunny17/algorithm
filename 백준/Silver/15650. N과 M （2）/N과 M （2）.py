from itertools import combinations

N, M = map(int, input().split())
numbs = [x for x in range(1, N+1)]

lst = list(combinations(numbs, M))

for i in lst:
    rlt = ' '.join(map(str, i))
    print(rlt)