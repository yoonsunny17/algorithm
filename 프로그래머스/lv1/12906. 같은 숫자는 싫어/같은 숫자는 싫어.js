function solution(arr)
{
    let answer = [];
    
    for (let i=1; i<arr.length+1; i++){
        if (arr[i-1] !== arr[i]){
            answer.push(arr[i-1])
        }
    }
    
    return answer
}