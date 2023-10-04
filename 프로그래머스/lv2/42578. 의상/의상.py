def solution(clothes):
    ans = 1
    dic = dict()
    
    for c in clothes:
        # dic의 key가 아니면 일단 추가하고, key이면 value값 +1 해주기
        if c[1] not in dic.keys():
            dic[c[1]] = 1
        else:
            dic[c[1]] += 1

    for d in dic.values():
        ans += d * ans
        
    return ans - 1