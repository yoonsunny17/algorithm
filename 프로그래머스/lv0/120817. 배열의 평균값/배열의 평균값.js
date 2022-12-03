function solution(numbers) {
    var answer = 0;
    for (i of numbers) {
        answer += i
    }
    return answer / numbers.length;
}