def solution(elements):
    answer = set()
    
    n = len(elements)
    elements = elements * 2
    
    for i in range(n):
        for j in range(n):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)