H, W = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0

for i in range(1, W-1):
    left_height = max(heights[:i])
    right_height = max(heights[i+1:])

    shorter = min(left_height, right_height)

    if heights[i] < shorter:
        ans += shorter - heights[i]

print(ans)