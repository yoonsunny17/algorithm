import sys
from itertools import combinations
    
N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rlt = float('inf')

# 존재하는 치킨집, 집 담아주기
chickens, houses = [], []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chickens.append([i, j])
        elif matrix[i][j] == 1:
            houses.append([i, j])

# 선택받은 치킨집들
for selected in combinations(chickens, M):
    chicken_street = [] # 각 집들의 치킨거리를 담아 줄 리스트

    # 각 집에 대해서, 선택된 치킨가게들 중 어디가 제일 가까운지 확인해보자
    for house in houses:
        min_d = float('inf') # 집 하나에 대해서 치킨거리 찾아줄 변수
        for kkk in selected:
            dis = abs(house[0]-kkk[0]) + abs(house[1]-kkk[1])
            min_d = min(dis, min_d)

        chicken_street.append(min_d)
    rlt = min(rlt, sum(chicken_street))

print(rlt)