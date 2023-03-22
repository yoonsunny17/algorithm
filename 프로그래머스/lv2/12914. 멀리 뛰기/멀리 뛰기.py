def solution(n):
    
    # n = 1: return 1, n = 2: return 2
    if n < 3:
        return n
    
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
            
    return dp[n] % 1234567