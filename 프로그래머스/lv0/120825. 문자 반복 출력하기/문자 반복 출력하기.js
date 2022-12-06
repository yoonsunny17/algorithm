function solution(my_string, n) {
    const arr = []
    const answer = my_string.split("")
    for (i of answer) {
        arr.push(i.repeat(n))
    }
    return arr.join("")
    
}