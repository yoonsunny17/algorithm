def jump(N, numbs):
    for i in range(N):
        # 현재 칸에서 점프 가능한 범위만큼 탐색
        for j in range(1, numbs[i]+1):
            if i + j < N: # 아직 도달하지 않은 경우에 점프 횟수 업데이트
                dp[i + j] = min(dp[i + j], dp[i]+1)
        
    # 마지막 칸에 도달 가능한지 확인해줘
    return dp[-1] if dp[-1] != float('inf') else -1 

N = int(input())
numbs = list(map(int, input().split()))
dp = [float('inf')] * N
dp[0] = 0

print(jump(N, numbs))