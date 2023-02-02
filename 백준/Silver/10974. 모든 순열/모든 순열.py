from itertools import permutations

n = int(input())
numbs = [x for x in range(1, n+1)]

for permu in permutations(numbs, n):
    print(' '.join(map(str, permu)))