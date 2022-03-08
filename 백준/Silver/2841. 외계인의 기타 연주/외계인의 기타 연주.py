import sys
input = lambda: sys.stdin.readline().strip()

N, P = map(int, input().split())
melody = [list(map(int, input().split())) for i in range(N)]

cnt = 0
stack = [[] for i in range(7)]

for i, j in melody:
    if len(stack[i]) == 0:
        stack[i].append(j)
        cnt += 1
    else:
        # 더 높은 음을 눌러야 하는 경우
        if j > stack[i][-1]:
            stack[i].append(j)
            cnt += 1
        # 이미 누르고 있는 경우
        elif j == stack[i][-1]:
            continue
        # 낮은 음으로 돌아가야 하는 경우
        else:
            while len(stack[i]) != 0 and j < stack[i][-1]:
                stack[i].pop()
                cnt += 1
            if len(stack[i]) != 0 and stack[i][-1] == j:
                continue
            stack[i].append(j)
            cnt += 1

print(cnt)
