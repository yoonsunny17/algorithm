function solution(array, commands) {
    let answer = [];
    
    commands.forEach(command => {
        const arr = array.slice(command[0]-1, command[1]).sort((a, b) => a-b);
        const pickedNum = arr[command[2]-1];
        answer.push(pickedNum)
    });
    return answer;
}