def solution(participant, completion):
    participant.sort()
    completion.sort()
        
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # null인 경우 배열의 맨 마지막 값 출력
    return participant[len(participant)-1]