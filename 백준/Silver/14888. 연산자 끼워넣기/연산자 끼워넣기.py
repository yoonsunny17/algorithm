def dfs(i, rlt, add, sub, mul, div):
    global max_rlt, min_rlt

    if i == N:
        max_rlt = max(max_rlt, rlt)
        min_rlt = min(min_rlt, rlt)
        return

    if add > 0:
        dfs(i+1, rlt+numbs[i], add-1, sub, mul, div)
    if sub > 0:
        dfs(i+1, rlt-numbs[i], add, sub-1, mul, div)
    if mul > 0:
        dfs(i+1, rlt*numbs[i], add, sub, mul-1, div)
    if div > 0:
        dfs(i+1, -((-rlt)//numbs[i]) if rlt < 0 else (rlt//numbs[i]), add, sub, mul, div-1)

N = int(input())
numbs = list(map(int, input().split()))
op = list(map(int, input().split()))

max_rlt = -10**9
min_rlt = 10**9

dfs(1, numbs[0], op[0], op[1], op[2], op[3])
print(f'{max_rlt}\n{min_rlt}')