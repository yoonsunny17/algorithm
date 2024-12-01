const solution = (num_list) => {
    let answer = [0, 0]
    
    for (let i=0; i<num_list.length; i++) {
        if (num_list[i] % 2) {
            answer[1]++
        } else answer[0]++
    }
    
    return answer
}




// function solution(num_list) {
//     answer = [0, 0]
//     for (let a of num_list) {
//         answer[a%2]++
//     }
//     return answer
// }
