def back(i, calc, add, sub, mlt, div):
    global max_v, min_v
    if i == N:
        max_v = max(max_v, calc)
        min_v = min(min_v, calc)
        return

    # 아직 연산자가 남아있는 경우 계산해주기
    if add > 0:
        back(i+1, calc+numbs[i], add-1, sub, mlt, div)
    if sub > 0:
        back(i+1, calc-numbs[i], add, sub-1, mlt, div)
    if mlt > 0:
        back(i+1, calc*numbs[i], add, sub, mlt-1, div)
    if div > 0:
        back(i+1, -((-calc)//numbs[i]) if calc < 0 else calc//numbs[i], add, sub, mlt, div-1)

N = int(input())
numbs = list(map(int, input().split()))
op = list(map(int, input().split()))

max_v, min_v = -10**9, 10**9 # 최댓값, 최솟값 limit 설정

# 처음에 이미 첫번째 숫자 넣어서 계산 시작하니까 i = 0 부터 시작
back(1, numbs[0], op[0], op[1], op[2], op[3])

print(f'{max_v}\n{min_v}')