def solution(board, h, w):
    answer = 0
    
    # 상 하 좌 우 
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for i in range(4):
        rr = h + dr[i]
        cc = w + dc[i]
        
        if 0 <= rr < len(board[0]) and 0 <= cc < len(board[0]) and board[rr][cc] == board[h][w]:
            answer += 1
    return answer