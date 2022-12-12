function solution(numbers) {
    // var answer = 0;
    // return answer;
    let dict = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    dict.forEach((el, idx) => {
        numbers = numbers.replaceAll(el, idx)
    })
    
    return Number(numbers)
}