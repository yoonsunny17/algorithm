def solution(ineq, eq, n, m):
    answer = True
    
    if ineq == '>' and eq == '=':
        answer = n >= m
    elif ineq == '>' and eq == '!':
        answer = n > m
    elif ineq == '<' and eq == '=':
        answer = n <= m
    else:
        answer = n < m
        
    return 1 if answer else 0