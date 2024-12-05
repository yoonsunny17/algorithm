// 1. match 정규식 사용하기
// function solution(order) {
//     // 369 아무것도 가지고 있지 않는 경우 0 출력해줘!
//     return order.toString().match(/[369]/g).length ?? 0
// }

// 2. set, has 사용하기
function solution(order) {
    const s = new Set('369')
    return order.toString().split('').filter(v => s.has(v)).length
}


// function solution(order) {
//     let answer = 0;
//     const orderNum = [...order.toString()]
    
//     for (num of orderNum) {
//         if (['3', '6', '9'].includes(num)) {
//             answer++
//         }
//     }
    
//     return answer
// }


// function solution(order) {
//     var answer = 0;
//     const numbs = order.toString().split('')
//     for (numb of numbs) {
//         if (numb == '3' || numb == '6' || numb == '9') {
//             answer += 1
//         }
//     }
//     return answer;
// }