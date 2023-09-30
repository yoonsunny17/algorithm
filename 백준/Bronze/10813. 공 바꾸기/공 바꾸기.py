n, m = map(int, input().split())

baskets = [i for i in range(n+1)]

for k in range(m):
    a, b = map(int, input().split())
    baskets[a], baskets[b] = baskets[b], baskets[a]

for j in range(1, len(baskets)):
    print(baskets[j], end=' ')