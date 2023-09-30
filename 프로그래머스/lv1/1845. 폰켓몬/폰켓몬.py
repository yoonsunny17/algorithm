def solution(nums):
    mine = len(nums) // 2
    kinds = len(set(nums))
    
    return min(kinds, mine)


# def solution(nums):
#     want = len(nums) // 2  # 내가 뽑고 싶은 포켓몬 수
#     kinds = len(set(nums))  # 포켓몬 종류 개수
    
#     # 종류가 다양하면 내가 뽑고 싶은 포켓몬 수만큼 종류 다양하게 뽑을 수 있음
#     return want if kinds >= want else kinds