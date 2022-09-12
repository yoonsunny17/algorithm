H, W = map(int, input().split())
pillars = list(map(int, input().split()))

ans = 0

for i in range(1, W-1):
    left_pillar = max(pillars[:i])
    right_pillar = max(pillars[i+1:])

    short_pillar = min(left_pillar, right_pillar)

    if pillars[i] < short_pillar:
        ans += short_pillar - pillars[i]
    
print(f'{ans}')