N = int(input())
numbs = list(map(int, input().split()))

cnt = 0
for numb in numbs:
    for i in range(2, numb+1):
        if numb % i == 0:
            if numb == i:
                cnt += 1

            break

print(cnt)