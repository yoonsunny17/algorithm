def solution(cards1, cards2, goal):
    c1, c2 = len(cards1), len(cards2)
    idx1, idx2 = 0, 0
    
    for g in goal:
        if idx1 < len(cards1) and g == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and g == cards2[idx2]:
            idx2 += 1
        else:
            return "No"
    return "Yes"