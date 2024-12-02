function solution(rsp) {
    const win = {
        "2": "0",
        "0": "5",
        "5": "2"
    }
    
    return rsp.split('').map(v => win[v]).join("")
}


// function solution(rsp) {
//     const win = {
//         2: 0,
//         0: 5,
//         5: 2
//     }
    
//     return [...rsp].reduce((acc, curr) => acc+win[curr], '')
// }