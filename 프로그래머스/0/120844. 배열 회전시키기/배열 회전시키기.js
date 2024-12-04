function solution(numbers, direction) {
    if (direction === 'right') {
        // 마지막 원소를 앞으로 끌어온다
        numbers.unshift(numbers.pop())
    } else {
        // 첫번째 원소를 마지막에 붙인다
        numbers.push(numbers.shift())
    }
    
    return numbers
}


// function solution(numbers, direction) {
//     if (direction === "right") {
//         numbers.unshift(numbers.pop())
//     } else {
//         numbers.push(numbers.shift())
//     }
//     return numbers
// }