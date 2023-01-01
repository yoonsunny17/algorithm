function solution(left, right) {
    let answer = 0
    
    for (let i = left; i <= right; i++){
        counts(i) % 2 === 0 ? answer += i : answer -= i
    }
    
    return answer
}

function counts(numb) {
    let count = 0
    for (let i = 1; i <= numb; i++){
        if (numb % i === 0) {
            count++
        }
    }
    
    return count
}