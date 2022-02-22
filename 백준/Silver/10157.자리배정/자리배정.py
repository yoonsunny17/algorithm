C, R = map(int, input().split())
K = int(input())

# row = C, column = R 인 이차원 리스트 만들기. 모든 요소를 0으로 만들자
matrix = [[0] * R for _ in range(C)]
# pprint(matrix)

# 일단은 달팽이처럼 delta 만들고, 우 하 좌 상 순서로 꺾으면서 숫자 넣어주자
r = c = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
idx = 0
# x = y = 0

for n in range(1, C * R + 1):
    matrix[r][c] = n
    r += dr[idx]
    c += dc[idx]

    # idxError 방지 또는 이미 값이 들어있는 경우 방향 바꿔줘
    if r < 0 or c < 0 or r >= C or c >= R or matrix[r][c] != 0:
        # idx 초기화 해주고,
        r -= dr[idx]
        c -= dc[idx]

        # 뺑뺑이 코드
        idx = (idx + 1) % 4
        r += dr[idx]
        c += dc[idx]

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == K:
            print(f'{r+1} {c+1}')

if K > R*C:
    print(f'{0}')