function solution(order) {
    var answer = 0;
    const numbs = order.toString().split('')
    for (numb of numbs) {
        if (numb == '3' || numb == '6' || numb == '9') {
            answer += 1
        }
    }
    return answer;
}