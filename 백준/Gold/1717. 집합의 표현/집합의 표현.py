import sys
from collections import deque
sys.setrecursionlimit(100000)

def union(x, y):
    i = find(x)
    j = find(y)

    parent[max(i, j)] = min(i, j)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


n, m = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
parent = [x for x in range(n+1)]  # 0 부터 n까지 !
q = deque(info)

while q:
    check, a, b = q.popleft()
    if check == 0:
        union(a, b)
    if check == 1:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')