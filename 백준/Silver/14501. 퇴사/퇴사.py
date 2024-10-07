N = int(input())

t_arr, p_arr = [], []
dp = [0] * (N+1)
for _ in range(N):
    T, P = map(int, input().split())
    t_arr.append(T)
    p_arr.append(P)

# 거꾸로 계산해보자
for i in range(N-1, -1, -1):
    # 만약 i일에 일을 했다고 가정했을 때, N일을 넘어선다면 그 전날이랑 같은 수익으로 생각
    if i + t_arr[i] > N:
        dp[i] = dp[i+1]
    # 넘어서지 않는다면, 일을 하지 않은 경우와 일을 해서 수익이 생긴 경우 중에 어느 경우가 더 효율적인지 생각
    else:
        dp[i] = max(dp[i+1], p_arr[i] + dp[i+t_arr[i]])

print(dp[0])