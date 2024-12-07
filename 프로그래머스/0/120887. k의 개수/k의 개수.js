function solution(i, j, k) {
    let s = '';
    for (i; i<=j; i++) {
        s += i
    }
    return s.split(k).length - 1
}


// function solution(i, j, k) {
//     let s = ''
    
//     for (i; i<=j; i++) {
//         s += i
//     }
    
//     return s.split('').filter(v => Number(v) === k).length
// }




// function solution(i, j, k) {
//     var answer = []
//     for (let a=i; a<=j; a++) {
//         answer.push(a)
//     }
//     return answer.join('').split('').filter(a => a==k).length
// }