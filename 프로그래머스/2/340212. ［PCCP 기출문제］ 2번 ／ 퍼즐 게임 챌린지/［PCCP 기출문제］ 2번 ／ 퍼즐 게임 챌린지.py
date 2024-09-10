def solution(diffs, times, limit):

    def find_lower(level):
        total_time, time_prev = 0, 0

        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]

            # 난이도가 숙련도보다 낮거나 같으면 안틀려
            if diff <= level:
                total_time += time_cur
            else:
                total_time += (time_cur + time_prev) * (diff - level) + time_cur

            # 방금 걸린 시간 = 다음 문제 풀 때 틀릴 경우 더해줄 시간
            time_prev = time_cur

            # 만약에 이미 limit을 초과했다면 return
            if total_time > limit:
                return total_time

        return total_time
    
    # 이분탐색 범위: diffs 최솟값 ~ 최댓값
    start, end = min(diffs), max(diffs)
    while start < end:
        mid = (start + end) // 2
        
        if find_lower(mid) <= limit:
            end = mid
        else:
            start = mid + 1
    
    return start
