N = int(input())
P = list(map(int, input().split()))
P.sort()
time = [0]*N

cnt = 0
for i in range(N):
    cnt += P[i]
    time[i] = cnt

rlt = 0
for t in time:
    rlt += t

print(rlt)