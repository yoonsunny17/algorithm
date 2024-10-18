import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while True:
        one = heapq.heappop(scoville)
        # 가장 안매운것이 K이상이라면 끝
        if one >= K:
            break
        # 리스트가 다 비었는데 K이상이 안되면 -1 리턴
        if not len(scoville):
            return -1
        
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one + two * 2)
        cnt += 1
        
    return cnt