def solution(numbers, n):
    answer = 0
    
    for numb in numbers:
        if answer > n:
            break
        answer += numb
    return answer