import sys

N, S = map(int, sys.stdin.readline().split())
numbs = list(map(int, sys.stdin.readline().split()))

start = 0
end = 1
interval_sum = numbs[0]
min_rlt = float("inf")

while True:
    if interval_sum >= S:
        if end - start < min_rlt:
            min_rlt = end - start
        interval_sum -= numbs[start]
        start += 1
    elif end == N:
        break
    else:
        interval_sum += numbs[end]
        end += 1

if min_rlt == float("inf"):
    print(0)
else:
    print(min_rlt)