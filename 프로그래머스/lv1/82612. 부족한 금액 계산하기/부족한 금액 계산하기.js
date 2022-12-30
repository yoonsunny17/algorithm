function solution(price, money, count) {
//     var answer = -1;

//     return answer;
    let need = 0
    for (let i = 1; i <= count; i++){
        need += i
    }
    need *= price
    
    if (need - money > 0){
        return need - money
    } else {
        return 0
    }
}