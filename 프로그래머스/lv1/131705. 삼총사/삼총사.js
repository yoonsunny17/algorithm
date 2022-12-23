function solution(number) {  
    let answer = 0
    
    const combination = (numbs, start) => {
        if (numbs.length === 3){
            answer += numbs.reduce((acc, cur) => acc + cur, 0) === 0 ? 1 : 0;
            return;
        }
        
        for (let i = start; i < number.length; i++){
            combination([...numbs, number[i]], i+1)
        }
    }
    combination([], 0);
    return answer
}