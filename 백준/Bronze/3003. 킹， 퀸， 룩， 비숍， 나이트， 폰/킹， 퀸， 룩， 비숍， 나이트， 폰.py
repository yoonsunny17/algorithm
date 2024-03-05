curr = list(map(int, input().split()))

origin = [1, 1, 2, 2, 2, 8]

for i in range(len(curr)):
    print(origin[i] - curr[i], end=' ')