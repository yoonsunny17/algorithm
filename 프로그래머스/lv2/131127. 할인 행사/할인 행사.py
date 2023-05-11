from collections import Counter

def solution(want, number, discount):
    ans = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]):
            ans += 1
    return ans


# def solution(want, number, discount):
#     ans = 0
    
#     for i in range(len(discount)):
#         ten = discount[i:i+10]
#         if len(ten) == 10:
#             cnt = 0
#             for j in range(len(want)):
#                 if ten.count(want[j]) != number[j]:
#                     break
#                 cnt += 1
#             if cnt == len(want):
#                 ans += 1
#     return ans