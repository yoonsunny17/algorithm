N = int(input())
numbs = list(map(int, input().split()))

ans, temp = 1, 1

for i in range(1, len(numbs)):
    if numbs[i-1] <= numbs[i]:
        temp += 1

    else :
        ans = max(ans, temp)
        temp = 1

ans = max(ans, temp)
temp =1

for i in range(1, len(numbs)):
    if numbs[i-1] >= numbs[i]:
        temp += 1
    else:
        ans = max(ans, temp)
        temp = 1

ans = max(ans, temp)

print(ans)