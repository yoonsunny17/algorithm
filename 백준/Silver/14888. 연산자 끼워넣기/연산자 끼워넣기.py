def dfs(i, rlt, add, sub, mlt, div):
    global max_rlt, min_rlt

    if i == N:
        max_rlt = max(max_rlt, rlt)
        min_rlt = min(min_rlt, rlt)
        return

    if add > 0:
        dfs(i+1, rlt+numbs[i], add-1, sub, mlt, div)
    if sub > 0:
        dfs(i+1, rlt-numbs[i], add, sub-1, mlt, div)
    if mlt > 0:
        dfs(i+1, rlt*numbs[i], add, sub, mlt-1 ,div)
    if div > 0:
        dfs(i+1, -((-rlt)//numbs[i]) if rlt < 0 else (rlt//numbs[i]), add, sub, mlt, div-1)


N = int(input())
numbs = list(map(int, input().split()))  # N개의 숫자
ops = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

max_rlt = -10**9
min_rlt = 10**9

dfs(1, numbs[0], ops[0], ops[1], ops[2], ops[3])

print(f'{max_rlt}\n{min_rlt}')