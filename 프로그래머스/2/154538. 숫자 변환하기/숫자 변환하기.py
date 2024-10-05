from collections import deque

def solution(x, y, n):
    q = deque([[x, 0]]) # [현재값, 연산 횟수]
    visited = set()
    
    while q:
        current, steps = q.popleft()
        
        if current == y:
            return steps
        
        if current > y:
            continue
        
        add_n = current + n
        if add_n not in visited and add_n <= 1000000:
            visited.add(add_n)
            q.append([add_n, steps+1])
            
        multiply_2 = current * 2
        if multiply_2 not in visited and multiply_2 <= 1000000:
            visited.add(multiply_2)
            q.append([multiply_2, steps+1])
            
        multiply_3 = current * 3
        if multiply_3 not in visited and multiply_3 <= 1000000:
            visited.add(multiply_3)
            q.append([multiply_3, steps+1])
    
    return -1