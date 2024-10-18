import math
from collections import deque

def solution(progresses, speeds):
    N = len(progresses)
    ans = []

    arr = deque() # 언제 배포가 가능한지
    for i in range(N):
        arr.append(math.ceil((100 - progresses[i]) / speeds[i]))

    curr = arr.popleft()
    cnt = 1
    while arr:
        tmp = arr.popleft()
        if curr < tmp: # 배포 해주고, 기준 갱신해준다
            ans.append(cnt)
            cnt = 1
            curr = tmp
        else: # cnt 더해주고, tmp 기준 바꾼다
            cnt += 1
    
    ans.append(cnt)
    return ans