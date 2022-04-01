from collections import deque
from itertools import combinations


def check(area):
    q = deque()
    visited = [0] * (N + 1)
    q.append(area[0])
    visited[area[0]] = 1

    while q:
        v = q.popleft()
        for j in graph[v]:
            if j in area and not visited[j]:
                visited[j] = 1
                q.append(j)

    return visited


def calc(A, B):
    p1, p2 = 0, 0
    for a in A:
        p1 += population[a-1]
    for b in B:
        p2 += population[b-1]

    p = abs(p1 - p2)
    return p


N = int(input())
population = list(map(int, input().split()))
numbs = [x for x in range(1, N+1)]
graph = [[] for _ in range(N+1)]
rlt = []

for i in range(1, N+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

for k in range(1, N//2+1):
    for area_1 in combinations(numbs, k):
        area_2 = tuple(set(numbs).difference(area_1))
        
        if sum(check(area_1)) + sum(check(area_2)) == N:
            rlt.append(calc(area_1, area_2))

if not len(rlt):
    print(-1)
else:
    print(min(rlt))