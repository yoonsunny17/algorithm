N, S = map(int, input().split())
numbs = list(map(int, input().split()))

start = 0
end = 1
interval_sum = numbs[0]
min_len = float('inf')

while True:
    if interval_sum >= S:
        if end - start < min_len:
            min_len = end - start
        
        interval_sum -= numbs[start]
        start += 1
    
    elif end == N:
        break

    else:
        interval_sum += numbs[end]
        end += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)