def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        sec = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]: # 가격이 떨어지지 않았다면
                sec += 1
            else: # 가격이 떨어진 순간 종료
                break
        answer.append(sec) # 몇초 유지되었는지를 넣어주기
    answer.append(0) # 맨 마지막은 무조건 0초
    
    return answer