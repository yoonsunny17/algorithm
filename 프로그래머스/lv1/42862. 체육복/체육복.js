function solution(n, lost, reserve) {
    // 체육복을 입을 수 있는 학생의 수
    let answer = n - lost.length
    
    let stolen = lost.sort((a,b) => a-b).filter((el) => !reserve.includes(el))
    let extra = reserve.sort((a,b) => a-b).filter((el) => !lost.includes(el))
    
    // 여벌의 체육복 가져왔는데 도난 당한 경우
    reserve.forEach((el) => {
        console.log(el)
        if (lost.includes(el)){
            answer++
        }
    })
    
    // 체육복 없는 친구들 만큼 빌려주는 행동을 반복할거야
    for (let i=0; i<lost.length; i++){
        // 만약에 여벌의 체육복 있는 친구의 왼쪽 친구가 체육복이 없다면
        if (extra.includes(stolen[i]-1)){
            answer++
            extra = extra.filter((el) => el !== stolen[i]-1)
        } else if (extra.includes(stolen[i]+1)){
        // 만약에 여벌의 체육복 있는 친구의 오른쪽 친구가 체육복이 없다면
            answer++
            extra = extra.filter((el) => el !== stolen[i]+1)
        }
    }
    return answer
}