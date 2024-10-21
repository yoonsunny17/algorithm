K, N = map(int, input().split())
wires = [int(input()) for _ in range(K)]

start, end = 1, max(wires)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for wire in wires:
        cnt += (wire // mid)

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)