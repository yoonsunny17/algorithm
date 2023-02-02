from collections import deque

def solution(progresses, speeds):
    n = len(progresses)
    days = deque()  # 총 며칠 더 일해야 하는지 담아줄 큐
    for i in range(n):
        rest = 100 - progresses[i]
        
        # 만약 speed로 나눈 값이 나누어 떨어진다면 몫만큼 일하고
        # 아니라면 +1 일 추가
        if (rest % speeds[i] == 0):
            days.append(rest//speeds[i])
        else:
            days.append(rest//speeds[i] + 1)
    
    print(days)
    answer = []  # 최종 출력해 줄 리스트
    cnt = 1
    while days:
        # cnt 가 2 이상이면 1 차감하고 days pop 해주고 다음 단계로 넘어가주기
        if cnt > 1:
            cnt -= 1
            days.popleft()
            continue
            
        temp = days.popleft()
        for day in days:
            if temp >= day:
                cnt += 1
            else:
                break
        answer.append(cnt)
    
    return answer