N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])

info.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end_time = info[0][1]

for i in range(1, N):
    if info[i][0] >= end_time:
        cnt += 1
        end_time = info[i][1]

print(cnt)