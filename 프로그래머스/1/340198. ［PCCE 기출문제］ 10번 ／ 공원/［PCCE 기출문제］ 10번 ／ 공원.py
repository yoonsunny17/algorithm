def can_place_mat(park, size, x, y):
    # 주어진 위치에서 size x size 크기 돗자리 놓을 수 있는지 확인
    rows = len(park)
    cols = len(park[0])
    
    # 범위 유효한지 확인
    if x + size > rows or y + size > cols:
        return False
    
    # size x size 영역에 사람이 없는지 확인
    for i in range(x, x+size):
        for j in range(y, y+size):
            if park[i][j] != "-1":
                return False
    
    return True

def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    mats.sort(reverse=True) # 큰 사이즈부터 확인
    
    # 각 돗자리 크기에 대해
    for size in mats:
        # 모든 위치에서 확인
        for i in range(rows):
            for j in range(cols):
                if can_place_mat(park, size, i, j):
                    return size
                
    return -1