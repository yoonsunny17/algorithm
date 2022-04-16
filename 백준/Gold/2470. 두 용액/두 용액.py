import sys

N = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split()))
info.sort()

start = 0
end = N - 1

min_cnt = float('inf')
sol1, sol2 = 0, 0

while start < end:
    if abs(info[start] + info[end]) < min_cnt:
        min_cnt = abs(info[start] + info[end])
        sol1 = info[start]
        sol2 = info[end]

    else:
        if info[start] + info[end] < 0:
            start += 1
        else:
            end -= 1

print(f'{sol1} {sol2}')
