from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

rlt = set()

for per in permutations(cards, k):
    rlt.add(''.join(per))

print(len(rlt))