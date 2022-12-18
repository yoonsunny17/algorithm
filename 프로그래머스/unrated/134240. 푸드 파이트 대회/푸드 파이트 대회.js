function solution(food) {
    let answer = ''
    let arr = []
    for (let i=1; i<food.length; i++){
        arr.push(Math.floor(food[i]/2))
    }

    for (let i=0; i<arr.length; i++){
        answer += (i+1).toString().repeat(arr[i])
    }
    
    reverse = answer.split('').reverse().join('')
    answer += 0
    
    return answer += reverse
}