n, m = map(int, input().split())
j = int(input())

start, end = 1, m
distance = 0

for _ in range(j):
    apple = int(input())

    if apple >= start and apple <= end:
        continue

    if apple < start:
        distance += start - apple
        start = apple
        end = apple + m - 1

    elif apple > end:
        distance += apple - end
        start = apple - m + 1
        end = apple
    
print(distance)