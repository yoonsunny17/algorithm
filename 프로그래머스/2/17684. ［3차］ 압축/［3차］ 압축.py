def solution(msg):
    # 문자열 색인 번호 담아줄 결과 리스트
    rlt = []
    
    # 초기 사전 초기화
    dictionary = {chr(65+i):i+1 for i in range(26)}
    
    # 다음에 추가될 사전 색인 번호 (init=27)
    next_idx = 27
    
    # 현재 처리중인 문자열
    curr = ""
    
    for char in msg:
        tmp = curr + char # 현재 문자와 그 다음 문자 합해진 문자열 tmp로 생성
        
        # tmp가 사전에 존재한다면 curr 업데이트
        if tmp in dictionary:
            curr = tmp
        else:
            # 사전에 없는 경우 curr의 색인번호 출력
            rlt.append(dictionary[curr])
            # 새로운 문자열 사전에 추가
            dictionary[tmp] = next_idx
            next_idx += 1
    
            # 현재 탐색중인 문자열 업데이트
            curr = char
    
    # 마지막 문자열 남았으므로 색인 번호 추가
    if curr:
        rlt.append(dictionary[curr])
        
    return rlt