from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)
    ans = 0
    
    for per in permutations(dungeons, N):
        power = k
        cnt = 0
        for p in per:
            if power >= p[0]:
                power -= p[1]
                cnt += 1
        if cnt > ans:
            ans = cnt

    return ans