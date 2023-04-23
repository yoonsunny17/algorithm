from collections import deque

def solution(priorities, location):
    queue = deque([i, v] for i, v in enumerate(priorities))
    ans = 0
    
    while True:
        temp = queue.popleft()
        # 큐 안에 우선순위가 더 높은게 존재하는 경우가 하나라도 있으면 true가 됨
        if any(temp[1] < q[1] for q in queue):
            queue.append(temp)
        else:
            ans += 1
            if temp[0] == location:
                return ans
