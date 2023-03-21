from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순으로 재정렬
    
    q = deque(people)
    # 두명 태울 수 있을 때를 생각해보자
    while len(q) > 1:
        # 가장 가벼운 사람 + 가장 무거운 사람 <= limit 일때가 최적이겠지
        if q[0] + q[-1] <= limit:
            # 이게 만족한다면 일단 무거운사람 제명하고
            q.popleft()
        # 맨앞에 가장 가벼운 사람도 빼주고, 그담에 +1 해줘
        q.pop()
        answer += 1
    
    if len(q) == 1:
        answer += 1
    return answer