def solution(n_str):
    while True:
        if n_str[0] != '0':
            break
        
        else:
            n_str = n_str[1:]
    
    return n_str