from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    while len(q) > 1:
        # 가장 가벼운 사람이랑 가장 무거운 사람이 함께 탈 수 있는 경우
        if q[0] + q[-1] <= limit:
            # 가장 무거운 사람 제거해주고
            q.popleft()
        answer += 1
        q.pop()
        
    # 이제 한명 남았으면 +1 해주고 리턴해주자
    if len(q) == 1:
        answer += 1
    return answer
