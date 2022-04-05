def promising(v):
    for i in range(v):
        if row[v] == row[i] or abs(row[v] - row[i]) == (v-i):
            return False  # 둘 수 없엉~

    return True


def dfs(v):
    global cnt

    if v == N:
        cnt += 1
        return

    else:
        for i in range(N):
            row[v] = i
            if promising(v):
                dfs(v+1)


N = int(input())
cnt = 0
row = [0] * N

dfs(0)

print(cnt)