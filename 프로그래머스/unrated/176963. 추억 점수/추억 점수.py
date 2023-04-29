def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))
    
    for p in photo:
        score = 0
        for i in p:
            score += info.get(i, 0)
            # if i in info:
            #     score += info[i]            
        answer.append(score)

    return answer