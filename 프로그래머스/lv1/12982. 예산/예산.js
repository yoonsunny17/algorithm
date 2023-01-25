function solution(d, budget) {
    var answer = 0;
    
    const arr = d.sort((a, b) => a-b)
    for (let i=0; i<d.length; i++){
    	if (arr[i] <= budget){
            answer++;
            budget -= arr[i];
        }
    }
    return answer;
}