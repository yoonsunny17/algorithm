def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(scores[0])
    
    # a: 내림차순, b: 오름차순
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_b, rank = 0, 1
    
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        if max_b <= score[1]:
            if wanho_sum < sum(score):
                rank += 1
            max_b = score[1]
            
    return rank