N, K = map(int, input().split())

arr = [x for x in range(1, N+1)]
answer = []
idx = 0 # 제거대상 인덱스 번호

for i in range(N):
    idx += K-1
    if idx >= len(arr):
        idx = idx % len(arr)

    answer.append(str(arr.pop(idx)))

print("<",", ".join(answer)[:],">", sep='')