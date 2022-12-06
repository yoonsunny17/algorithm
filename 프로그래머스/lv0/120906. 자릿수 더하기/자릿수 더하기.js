function solution(n) {
    var answer = 0;
    n = n.toString()
    for (let i = 0; i < n.length; i++) {
        answer += parseInt(n[i])
    }
    return answer;
}