function solution(i, j, k) {
    var answer = []
    for (let a=i; a<=j; a++) {
        answer.push(a)
    }
    return answer.join('').split('').filter(a => a==k).length
}