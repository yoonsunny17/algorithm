function solution(num) {
    let answer = 0
    
    if (num === 1) return 0;
    
    while (true) {
        num % 2 === 0 ? num = parseInt(num/2) : num = num * 3 + 1
        answer++
        if (num === 1) break;
    }
    
    return answer >= 500 ? -1 : answer
}