function solution(board, moves) {
    const basket = []  // stack
    let answer = 0
    
    moves.forEach(order => {
        const doll = select(board, order-1)
        if (doll){
            // 바구니 맨 위에 있는 인형이 방금 집은거랑 동일할 때
            if (basket[basket.length-1] === doll){
                // 맨 위에 있는거 제거하고 인형 두개 누적
                basket.pop()
                answer += 2
            } else {
                basket.push(doll)
            }
        }
    })
    
    return answer
}

function select(board, order) {
    for (let r=0; r<board.length; r++){
        // 아직 인형이 남아있다면 집어서 바구니에 넣기
        if (board[r][order] !== 0){
            // 방금 집은 인형 표시해주고, board에서 빈 상태로 바꾸기
            const doll = board[r][order]
            board[r][order] = 0
            return doll
        }
    }
}