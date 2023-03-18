'''
1. brown + yellow 사각형 = 전체 사각형
2. yellow 사각형 = 안쪽 사각형 (테두리 한 줄 빼준 너비)
3. 가로길이(wid) >= 세로길이(leng)
'''
def solution(brown, yellow):
    total = brown + yellow # 전체 사각형
    
    # total = 12 이면 1 * 12, 2 * 6, 3 * 4 ...
    for leng in range(3, total):
        wid = int(total / leng)
        
        # 위의 세 조건 다 만족하는 경우라면
        if (wid * leng == total) and (wid >= leng) and ((wid-2) * (leng-2) == yellow):
            answer = [wid, leng]
    return answer