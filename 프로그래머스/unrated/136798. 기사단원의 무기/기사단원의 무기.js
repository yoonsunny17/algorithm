const yacksu = (num) => {
    let count = 0
    for (let i = 1; i <= Math.floor(num/2); i++){
        if (num % i === 0) count++
    }
    return count + 1 
}

function solution(number, limit, power) {
    var answer = 0
    
    for (let i = 1; i <= number; i++) {
        const cnt = yacksu(i)
        cnt <= limit ? answer += cnt : answer+= power
    }
    return answer
}

