function solution(n) {
    let i = 1;
    let factorial = 1;
    
    while (factorial <= n) {
        i++
        factorial *= i
    }
    
    return i-1
}


// function solution(n) {
//     var answer = 0;
//     for (let i=1; i<=10; i++) {
//         if (n >= factorial(i)) {
//             answer = i
//             continue
//         } else {
//             break
//         }
//     }
//     return answer;
// }
    
// function factorial(num) {
//     if (num > 1) return num*factorial(num-1)
//     return num
// }