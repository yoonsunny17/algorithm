function solution(s) {
    let dict = {}
    let answer = ''

    // 각 알파벳이 몇개씩 들어있는지 체크
    Array(...s).sort().map(i => dict[i] === undefined ? dict[i] = 1 : dict[i] += 1)
    
    // 1개인 경우 answer에 더해주기    
    for (const [key, value] of Object.entries(dict)) {
        if (value === 1) {
            answer += key
        }
    }
    return answer
}



// function solution(s) {
//     // var answer = '';
//     // return answer;
//     const dict = {}
    
//     s.split("").forEach(a => dict[a] !== undefined ? dict[a]+= 1 : dict[a]=1)
    
//     console.log(dict)
    
//     return Object.entries(dict).map(a => a[1] === 1 ? a[0] : null).filter(a => a !== null).sort().join("")
// }