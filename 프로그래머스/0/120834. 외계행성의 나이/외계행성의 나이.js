function solution(age) {
    let chr = 'abcdefghij'
    
    return Array.from(age.toString()).map(v => chr[v]).join("")
}



// function solution(age) {
//     const arr = String(age).split('')
//     var answer = '';
    
//     for (let i=0; i<arr.length; i++) {
//         answer += String.fromCharCode(Number(arr[i]) + 97)
//     }
    
//     return answer;
// }