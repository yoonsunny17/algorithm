T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)

    if N <= 3:
        print(1)
        continue

    if 4 <= N <= 5:
        print(2)
        continue

    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2

    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    print(dp[N])