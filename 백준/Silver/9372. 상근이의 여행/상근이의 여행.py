def union(i, j):
    x = find(i)
    y = find(j)

    parent[max(x, y)] = min(x, y)


def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parent = [x for x in range(1+N)]
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
            cnt += 1

    print(cnt)