import sys

R, S = map(int, sys.stdin.readline().split())

before_collision = [sys.stdin.readline().rstrip() for _ in range(R)]
distance = float('inf')

for j in range(S):
    low_meteor = 0
    high_ground = float('inf')
    check = False  # 유성이 있는지 확인해주기 (처음에는 없음으로 설정)

    for i in range(R):
        if before_collision[i][j] == 'X':
            if i > low_meteor:
                low_meteor = i
                check = True  # 유성 발견했음을 체크!

        elif before_collision[i][j] == '#':
            if i < high_ground:
                high_ground = i

    if check:
        distance = min(abs(high_ground - low_meteor) - 1, distance)

after_collision = [list('.' for _ in range(S)) for _ in range(R)]
for i in range(R):
    for j in range(S):
        if before_collision[i][j] == 'X':
            after_collision[i+distance][j] = 'X'
        if before_collision[i][j] == '#':
            after_collision[i][j] = '#'

for i in range(R):
    for j in range(S):
        sys.stdout.write(after_collision[i][j])
    sys.stdout.write('\n')