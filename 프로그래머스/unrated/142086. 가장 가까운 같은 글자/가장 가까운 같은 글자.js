function solution(s) {
    var answer = [];
    var dict = {}
    
    for (let i = 0; i < s.length ; i++) {
        if (dict[s[i]] === undefined) {
            answer.push(-1)
        } else {
            answer.push(i - dict[s[i]])
        }
        dict[s[i]] = i
    }
    return answer;
}