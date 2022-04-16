N = int(input())
numbs = list(map(int, input().split()))
numbs.sort()
x = int(input())
start = 0
end = N - 1
interval_cnt = 0
cnt = 0

while start < end:
    interval_cnt = numbs[start] + numbs[end]
    if interval_cnt < x:
        start += 1

    elif interval_cnt > x:
        end -= 1

    else:
        cnt += 1
        start += 1

print(cnt)