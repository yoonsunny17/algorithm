function solution(numbers) {
    return numbers.reduce((a, c) => a+c, 0) / numbers.length
}


// function solution(numbers) {
//     var answer = 0;
//     for (i of numbers) {
//         answer += i
//     }
//     return answer / numbers.length;
// }