import sys
input = sys.stdin.readline

# n = 도시 개수, m = 버스 개수
n = int(input())
m = int(input())

inf = 987654321  # 비용 최댓값
# 이차원 리스트 만들고, 모든 비용을 최댓값으로 초기화
matrix = [[inf] * n for _ in range(n)]

# a = 버스 시작 도시, b = 버스 도착 도시, c = 한 번 타는데에 필요한 비용
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = min(matrix[a-1][b-1], c)

# 플로이드 워셜 구현
# a에서 b로 갈 때 k를 거쳐 가는 경우와 바로 가는 경우를 비교해서
# 최솟값으로 갱신해주기
for k in range(n):
    for a in range(n):
        for b in range(n):
            # 자기 자신을 거치는 경로 비용은 0으로 해주고
            if a == b:
                matrix[a][b] = 0
            # 나머지 경로는 최솟값으로 갱신해주기
            else:
                matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

# 무한대로 설정되어 있으면 0으로 초기화해주기
for i in range(n):
    for j in range(n):
        if matrix[i][j] == inf:
            matrix[i][j] = 0

for i in range(n):
    print(*matrix[i])
