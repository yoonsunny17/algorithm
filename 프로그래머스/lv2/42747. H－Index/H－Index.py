def solution(citations):
    arr = sorted(citations, reverse=True) # 인용 횟수 많은 것부터 정렬
    for i in range(len(arr)):
        if i >= arr[i]:
            return i
    
    return len(arr)