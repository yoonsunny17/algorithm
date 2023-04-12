# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if completion[i] != participant[i]:
#             return participant[i]
        
#     return participant[-1]

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]
    # return list(answer.keys())[0] # 위에랑 똑같이 나옴