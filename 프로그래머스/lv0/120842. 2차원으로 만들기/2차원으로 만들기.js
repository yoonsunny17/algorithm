function solution(num_list, n) {
    var answer = []
    for (let i=0; i < num_list.length;) {
        const temp = []
        for (let j=0; j < n; j++) {
            temp.push(num_list[i])
            i++
        }
        answer.push(temp)
    }
    return answer
}