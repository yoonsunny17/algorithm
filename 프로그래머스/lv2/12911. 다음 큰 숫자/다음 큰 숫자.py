def solution(n):
    maxN = 1000000
    for i in range(n+1, maxN+1): # 조건 1
        if format(i, 'b').count('1') == format(n, 'b').count('1'): # 조건 2
            return i