N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0 # 벌목된 나무 높이 합

    for tree in trees:
        if tree >= mid: # 나무가 더 높으면 잘리겠다
            cnt += tree - mid
    
    # 벌목 cnt와 target(M) 비교 이분탐색
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)