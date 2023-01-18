function solution(answers) {
    let answer = []
    let students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    let scores = [0, 0, 0]
    
    for (let i=0; i<students.length; i++){
        let rlt = 0
        
        for (let j=0; j<answers.length; j++){
            tmp = students[i][j % students[i].length]
            
            if (answers[j] === tmp) {
                rlt++
            }
        }
        scores[i] = rlt
    }
    
    for (let i=0; i<scores.length; i++){
        if (scores[i] === Math.max(...scores)){
            answer.push(i+1)
        }
    }
    return answer
}