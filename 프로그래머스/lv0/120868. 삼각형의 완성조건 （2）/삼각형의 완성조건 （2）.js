function solution(sides) {
    var answer = 0
    let maxlen = Math.max(...sides)
    let minlen = Math.min(...sides)
    
    for (let i=maxlen-minlen+1; i<=maxlen; i++) {
        answer++
    }
    
    for (let i=maxlen+1; i<maxlen+minlen; i++) {
        answer++
    }
    
    return answer
}