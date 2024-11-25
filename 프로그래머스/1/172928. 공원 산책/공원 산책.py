def solution(park, routes):
    N, M = len(park), len(park[0])
    
    # 동 서 남 북 (우 좌 하 상)
    move = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    si, sj = 0, 0
    
    # 시작 지점 잡아주기
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                si, sj = i, j
                
    # 각 명령 따르기
    for route in routes:
        direction, step = route.split(' ')
        
        step = int(step)
        di, dj = move[direction]
        
        flag = True
        ni, nj = si, sj
        
        for _ in range(step):
            ni += di
            nj += dj
            
            # 범위 밖이거나, X 인 경우 갈 수 없음 > flag를 False로 바꾸기
            if ni < 0 or ni >= N or nj < 0 or nj >= M or park[ni][nj] == 'X':
                flag = False
                break
                
        # 걸리지 않았다면 갈 수 있음
        if flag:
            si, sj = ni, nj
    
    return [si, sj]