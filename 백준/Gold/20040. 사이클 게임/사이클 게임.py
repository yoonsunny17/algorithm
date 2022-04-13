import sys
sys.setrecursionlimit(10*10)

def union(x, y):
    a = find(x)
    b = find(y)

    parent[max(a, b)] = min(a, b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


n, m = map(int, sys.stdin.readline().split())
parent = [x for x in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)