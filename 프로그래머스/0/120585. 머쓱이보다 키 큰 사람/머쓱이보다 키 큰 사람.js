function solution(array, height) {
    return array.filter((v) => v > height).length
}


// function solution(array, height) {
//     var answer = 0;
//     for (i of array) {
//         if (i > height) {
//             answer++
//         }
//     }
//     return answer;
// }