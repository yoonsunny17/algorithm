import sys
sys.setrecursionlimit(100000)

def union(x, y):
    a = find(x)
    b = find(y)

    parent[max(a, b)] = min(a, b)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

N = int(input())
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parent = [x for x in range(N)]

for i in range(N):
    for j in range(N):
        # 만약에 경로가 연결 되어있고, 서로 조상이 같지 않으면
        if matrix[i][j] and find(i) != find(j):
            # 유니온 연산 해줘!
            union(i, j)

# 중복 제거해주기 위해 set 사용
rlt = set()
for k in range(M):
    rlt.add(parent[plan[k] - 1])

# 길이가 1이다 = 모두의 조상이 같다 = 사이클이 이루어졌다
if len(rlt) == 1:
    print('YES')
else:
    print('NO')