function solution(num_list) {
    answer = [0, 0]
    for (let a of num_list) {
        answer[a%2]++
    }
    return answer
}
