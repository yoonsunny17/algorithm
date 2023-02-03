N = int(input())
M = int(input())
numbs = list(map(int, input().split()))

numbs.sort()  # 일단 정렬먼저 해주기

start, end = 0, N-1
temp = 0  # numbs[start] + numbs[end]
cnt = 0
# 두 인덱스 값이 같아지기 전까지
while start != end:
    temp = numbs[start] + numbs[end]
    # 만약 타겟 값과 동일하다면
    if temp == M:
        # 카운트 해주고, start를 왼쪽으로 옮기자
        cnt += 1
        start += 1
    # 만약 타겟값보다 크다면
    elif temp > M:
        # end를 왼쪽으로 옮기자
        end -= 1
    else:
        start += 1

print(cnt)