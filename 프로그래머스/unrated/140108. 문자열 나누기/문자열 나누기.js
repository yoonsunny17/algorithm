function solution(s) {
    let answer = 0;
    let x = 0  
    let y = 0  // x 가 아닌 다른 글자 횟수
    let alpha = ''  // x 글자
    
    for (let i of s) {
        // x 글자 뭔지 저장
        if (!alpha) alpha = i
        
        // 첫 글자가 i랑 같으면 x 증가, 아니면 y 증가 
        alpha === i ? x++ : y++
        
        // x 글자 나온 횟수가 다른 글자 횟수랑 같으면 초기화
        if (x === y) {
            answer++
            x = 0
            y = 0
            alpha = ''
        }
    }
    // 더이상 읽을 글자 없는 경우 나머지 처리
    if (alpha) answer++
    
    return answer
}