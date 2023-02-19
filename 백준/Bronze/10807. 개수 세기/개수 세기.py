n = int(input())
numbs = list(map(int, input().split()))
target = int(input())

ans = 0
for numb in numbs:
    if numb == target:
        ans += 1

print(ans)