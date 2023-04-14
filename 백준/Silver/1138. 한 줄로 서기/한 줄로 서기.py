N = int(input())
arr = list(map(int, input().split()))

rlt = [0] * N
for i in range(N):
    cnt = 0 # 내 왼쪽 빈자리 몇개인지 세어줄 변수
    for j in range(N):
        # 내 왼쪽 몇자리 비었는지 세어봤을 때, 조건을 충족하는 경우라면,
        # 비어있는 자리 확인하고 앉아
        if cnt == arr[i] and rlt[j] == 0:
            rlt[j] = i+1
            break
        # cnt가 아직 만족되지 않았고, 그 자리가 빈자리면, cnt +1 해줘
        elif cnt != arr[i] and rlt[j] == 0:
            cnt += 1

print(*rlt)