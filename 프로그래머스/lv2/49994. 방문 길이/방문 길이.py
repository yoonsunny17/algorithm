def solution(dirs):
    sets = set()
    y, x = 0, 0
    dr = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    
    for d in dirs:
        dy, dx = dr[d]
        yy = y + dy
        xx = x + dx
        if -5 <= yy <= 5 and -5 <= xx <= 5:
            sets.add(((y, x), (yy, xx)))  # 현재위치, 이동 후 위치
            sets.add(((yy, xx), (y, x)))  # 이동 후 위치, 현재 위치
            y = yy
            x = xx
            
    return len(sets) // 2  # 중복 제거해야함!