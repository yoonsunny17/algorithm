from collections import deque

def solution(priorities, location):
    answer = 0
    arr = [0] * len(priorities)
    arr[location] = 1
    q = deque(priorities)
    
    while True:
        # arr가 비어있거나, 최댓값이 0인 경우 = 원하는 값 출력된 경우
        if not arr or max(arr) == 0:
            break
        # 큐값 안의 최댓값이 첫번째 값일 때
        # 그 값 빼주고, arr값도 빼줘
        # 그리고 프로세스 한번 수행한 것 추가 +1
        if max(q) == q[0]:
            q.popleft()
            del arr[0]
            answer += 1
        # 원하는 목표값이 아닌 경우라면
        else:
            q.append(q[0])
            arr.append(arr[0])
            q.popleft()
            del arr[0]
    
    return answer
