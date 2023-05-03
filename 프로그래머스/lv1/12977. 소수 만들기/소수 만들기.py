# def solution(nums):
#     answer = -1

#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')

#     return answer

from itertools import combinations

def solution(nums):
    cnt = 0
    
    def solve(n):
        for i in range(2, n):
            if n % i == 0:
                return -1
        return n

    for combi in combinations(nums, 3):
        if solve(sum(combi)) != -1:
            cnt += 1
    return cnt