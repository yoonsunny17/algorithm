from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    
    cnt = 0  # 숫자들을 몇 번 움직였는지 세어 줄 변수

    while q:
        max_numb = max(q)
        front = q.popleft()
        m -= 1

        # 맨 앞에서 뽑은 숫자가 가장 큰 수인 경우
        if front == max_numb:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        
        # 맨 앞에서 뽑은 숫자가 가장 큰 수가 아닌 경우
        else:
            q.append(front)
            if m < 0:
                m = len(q) - 1
