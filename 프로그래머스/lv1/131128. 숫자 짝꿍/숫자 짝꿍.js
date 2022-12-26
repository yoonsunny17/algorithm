function solution(X, Y) {
    let answer = ''
    X = [...X]
    Y = [...Y]
    
    for (let i=0; i<10; i++){
        const currX = X.filter(el => Number(el) === i).length
        const currY = Y.filter(el => Number(el) === i).length
        answer += String(i).repeat(Math.min(currX, currY))
    }
    
    if (answer === "") return "-1"
    if (Number(answer) === 0) return "0"
    
    return answer.split("").sort((a, b) => Number(b)-Number(a)).join("")

   
    
}