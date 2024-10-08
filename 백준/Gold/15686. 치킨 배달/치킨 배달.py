from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
stores = []
house = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            stores.append([i, j])
        if matrix[i][j] == 1:
            house.append([i, j])

min_rlt = 987654321
distance = 0
for store in combinations(stores, M):
    chicken_street = []
    for home in house:
        min_d = []
        for kfc in store:
            distance = abs(home[0]-kfc[0]) + abs(home[1]-kfc[1])
            min_d.append(distance)

        chicken_street.append(min(min_d))
    min_rlt = min(min_rlt, sum(chicken_street))

print(min_rlt)