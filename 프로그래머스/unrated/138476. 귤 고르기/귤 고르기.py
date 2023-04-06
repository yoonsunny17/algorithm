from collections import Counter

def solution(k, tangerine):
    pick, ans = 0, 0
    kinds = Counter(tangerine)
    
    # i = 종류, j = 갯수, most_common(k) = 상위 k개의 원소 출력
    for i, j in kinds.most_common(k):
        k -= j
        ans += 1
        
        if k <= 0:
            return ans

# def solution(k, tangerine):
#     answer = 0
#     kinds = [0] * len(set(tangerine)) # 귤 종류 개수에 맞춰 리스트 생성
#     for tan in tangerine:
#         kinds[tan-1] += 1
    
#     kinds.sort(reverse=True) # 개수가 많은것부터 정렬
    
#     # i = idx, j = 갯수
#     for i, j in enumerate(kinds):
#         k -= j
#         answer += 1
#         if k <= 0:
#             return answer