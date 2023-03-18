def solution(s):
    zero = 0 # 0의 개수
    cnt = 0 # 이진 변환 몇번했는지
    
    # s가 1이 될 때까지 반복해줘 (s가 1이 아닌동안 무한 반복해줘)
    while s != "1":
        if "0" in s:
            zero += s.count("0")
            s = s.replace("0", "")
        
        length = len(s) # s의 길이
        s = str(format(length, 'b')) # 2진수로 변환해주기
        cnt += 1 # 이진 변환 횟수 세어줘
        
    return [cnt, zero]