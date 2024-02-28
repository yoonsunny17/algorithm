def solution(binomial):
    answer = 0
    arr = binomial.split(' ')
    
    a, op, b = int(arr[0]), arr[1], int(arr[2])
    
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b
        
    return answer