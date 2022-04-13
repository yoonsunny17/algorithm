import sys
sys.setrecursionlimit(100000)

def union(x, y):
    a = find(x)
    b = find(y)

    parent[max(a, b)] = min(a, b)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

N = int(input())
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parent = [x for x in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] and find(i) != find(j):
            union(i, j)

rlt = set()
for k in range(M):
    rlt.add(parent[plan[k] - 1])

if len(rlt) == 1:
    print('YES')
else:
    print('NO')