function solution(absolutes, signs) {
    let answer = 0
    
    for (let i = 0; i < signs.length; i++) {
        signs[i] === true ? answer += absolutes[i] : answer -= absolutes[i]
    }
    
    return answer
}