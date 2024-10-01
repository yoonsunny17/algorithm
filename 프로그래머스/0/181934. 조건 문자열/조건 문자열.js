function solution(ineq, eq, n, m) {
    var answer = true;
    
    if (ineq === '>' && eq === '=') {
        answer = n >= m
    } else if (ineq === '>' && eq === '!') {
        answer = n > m
    } else if (ineq === '<' && eq === '=') {
        answer = n <= m
    } else {
        answer = n < m
    }

    if (answer === true) return 1
    else return 0
}