function solution(s) {
    s = s.split(" ")
    let answer = ''
    let arr = []
    
    s.forEach((item) => {
        for (let i = 0; i < item.length; i++) {
            if (i % 2 === 0) {
                answer += item[i].toUpperCase()
            } else { answer += item[i].toLowerCase() }
        }
        arr.push(answer)
        answer = ''
    })
    return arr.join([' '])
}