N = int(input())
time, profit = [], []
dp = [0]*(N+1)
for j in range(1, N+1):
    Ti, Pi = map(int, input().split())
    time.append(Ti)
    profit.append(Pi)

for i in range(N-1, -1, -1):
    if time[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(profit[i] + dp[i+time[i]], dp[i+1])

print(dp[0])