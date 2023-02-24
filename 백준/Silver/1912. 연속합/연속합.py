n = int(input())
arr = list(map(int, input().split()))

rlt = [arr[0]]  # 일단 비교해주기 위해 초기값 넣어주기

for i in range(n-1):
    rlt.append(max(rlt[i]+arr[i+1], arr[i+1]))

print(max(rlt))