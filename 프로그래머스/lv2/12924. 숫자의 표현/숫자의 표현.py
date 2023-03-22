def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        tmp = 0 # 연속 숫자들 더해줄 변수
        for j in range(i, n+1):
            tmp += j
            if tmp == n: # 연속 합이 조건을 만족하는 경우,
                answer += 1
                break
            elif tmp > n: # 연속 합이 조건을 만족하지 않는 경우 = 항상 초과
                break
    return answer