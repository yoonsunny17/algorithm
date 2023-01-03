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

n, m = map(int, sys.stdin.readline().split())
parent = [x for x in range(n+1)]

for _ in range(m):
    check, a, b = map(int, sys.stdin.readline().split())

    # check 가 0이면 합집합 연산 고고 (union)
    if check == 0:
        union(a, b)
    
    # check 가 1이면 a, b가 같은 집합에 있는지 확인해주자 (find)
    if check == 1:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')