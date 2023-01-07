function solution(numbers) {
    let answer = []
    
    for (let i = 0; i < numbers.length - 1; i++){
        for (let j = i+1; j < numbers.length; j++){
            answer.includes(numbers[i]+numbers[j]) ? null : answer.push(numbers[i]+numbers[j])
        }
    }
    
    return answer.sort((a, b) => a-b)
}