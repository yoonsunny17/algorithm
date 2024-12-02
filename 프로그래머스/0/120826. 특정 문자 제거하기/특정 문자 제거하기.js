function solution(my_string, letter) {
    // 정규표현식 사용
    let reg = new RegExp(letter, 'g')
    return my_string.replace(reg, '')
}


// function solution(my_string, letter) {
//     return my_string.replaceAll(letter, "")
    
//     // const answer = my_string.split(letter).join('')
//     // return answer;
// }