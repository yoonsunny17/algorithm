import sys

N = int(sys.stdin.readline())
check = [True] * (N+1)
check[0], check[1] = 0, 0

prime_lst = []

if N == 1:
    print(0)
    exit()

for i in range(2, N+1):
    if check[i]:
        prime_lst.append(i)
    for j in range(i*i, N+1, i):
        check[j] = False

start = 0
end = 1
interval_sum = prime_lst[0]
cnt = 0

while True:
    if interval_sum >= N:
        if interval_sum == N:
            cnt += 1
        interval_sum -= prime_lst[start]
        start += 1

    elif end == len(prime_lst):
        break

    else:
        interval_sum += prime_lst[end]
        end += 1

print(cnt)