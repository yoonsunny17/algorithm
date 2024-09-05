import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    works = [-w for w in works] # 최대힙
    heapq.heapify(works)
    
    for _ in range(n):
        i = heapq.heappop(works) # 가장 작은 수(음수 기준) 뽑기
        i += 1
        heapq.heappush(works, i)
    
    for j in works:
        answer += j**2
        
    return answer