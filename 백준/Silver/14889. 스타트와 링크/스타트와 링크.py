from itertools import combinations

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
numbs = [x for x in range(1, N+1)]
min_rlt = float('inf')

for t1 in combinations(numbs, N//2):
    t2 = list(set(numbs).difference(t1))
    start, link = 0, 0
    for t in combinations(t1, 2):
        start += matrix[t[0]-1][t[1]-1]
        start += matrix[t[1]-1][t[0]-1]
    for t in combinations(t2, 2):
        link += matrix[t[0]-1][t[1]-1]
        link += matrix[t[1]-1][t[0]-1]

    min_rlt = min(min_rlt, abs(start - link))

print(min_rlt)