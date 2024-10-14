import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * 301 # 계단 개수가 300 이하로 주어짐

if len(stairs) == 1:
    print(stairs[0])

elif len(stairs) == 2:
    print(stairs[0] + stairs[1])

elif len(stairs) == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[N-1])