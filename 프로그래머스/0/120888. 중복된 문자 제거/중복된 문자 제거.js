// python에서의 set과 달리 javascript에서의 set은 순서를 보장한다.

function solution(my_string) {
    return [...new Set(my_string)].join('')
}

// function solution(my_string) {
//     let answer = ''
    
//     for (let i=0; i<my_string.length; i++) {
//         if (!answer.includes(my_string[i])) {
//             answer += my_string[i]
//         } 
//     }
    
//     return answer
// }


// function solution(my_string){  
//     let answer="";
//     for(let i=0; i<my_string.length; i++){
//       if(my_string.indexOf(my_string[i])===i) answer+=my_string[i];
//     }
//     return answer;
// }
    