def solution(topping):
    N = len(topping)
    
    one = set()
    two = {}
    
    cnt = 0
    # 처음에는 모든 토핑이 두번째에 있음
    for i in topping:
        two[i] = two.get(i, 0) + 1
        
    # 각 위치에서 잘랐을 때 양쪽의 토핑 종류 수를 비교
    for i in range(N-1):
        # 현재 토핑을 첫번째로 이동
        one.add(topping[i])
        
        # 두번째에서 현재 토핑 개수 감소
        two[topping[i]] -= 1
        if two[topping[i]] == 0:
            del two[topping[i]]
            
        # 양쪽의 토핑 종류 수가 같으면 cnt 증가
        if len(one) == len(two):
            cnt += 1
    
    return cnt