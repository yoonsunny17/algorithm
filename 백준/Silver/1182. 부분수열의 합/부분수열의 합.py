import sys
from itertools import combinations

def sol(cnt):
    for i in range(1, N+1):
        for combi in combinations(numbs, i):
            if sum(combi) == S:
                cnt += 1
    return cnt

N, S = map(int, sys.stdin.readline().split())
numbs = list(map(int, sys.stdin.readline().split()))
print(sol(0))