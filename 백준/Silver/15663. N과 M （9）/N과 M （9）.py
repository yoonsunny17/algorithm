from itertools import permutations

N, M = map(int, input().split())
numbs = list(map(int, input().split()))
numbs = list(permutations(numbs, M))
numbs = sorted(list(set(numbs)))
for numb in numbs:
    print(*numb)