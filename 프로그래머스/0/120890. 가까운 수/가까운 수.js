function solution(array, n) {
    array.sort((a, b) => a - b) // 오름차순으로 정렬하고 시작
    
    let cnt = Infinity // 두수의 차
    let rlt = 0
    
    for (let i of array) {
        if (Math.abs(n-i) < cnt) {
            cnt = Math.abs(n-i)
            rlt = i
        }
    }
    
    return rlt
}



// function solution(array, n) {
//    return [...array].filter(a => Math.abs(a-n) === Math.min(...array.map(a => Math.abs(a-n)))).sort((a,b) => a-b)[0]

// }