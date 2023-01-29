function solution(s, n) {
    let answer = []
    s = s.split('')
    for (let i of s){
        i = i.charCodeAt(0)
        // 공백이면 그냥 공백
        if (i === 32){
            answer.push(String.fromCharCode(32))
        } else if (i >= 65 && i <= 90){
            // 대문자인 경우 대문자만
            (i+n > 90) ? answer.push(String.fromCharCode(i+n-26)) : answer.push(String.fromCharCode(i+n))
        } else if (i >= 97 && i <= 122){
            
            // 소문자인 경우 소문자만
            (i+n > 122) ? answer.push(String.fromCharCode(i+n-26)) : answer.push(String.fromCharCode(i+n))
        }
    }
    
    return answer.join('')
}