function solution(a, b, n) {
    var answer = 0
    while (n/a >= 1) {
        let free = parseInt(n/a)*b
        answer += free
        n = free + n%a
    }
    
    return answer
}