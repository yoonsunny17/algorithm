function solution(s) {
    s = s.split(" ")
    while(s.includes("Z")) {
        s.splice(s.indexOf("Z")-1, 2)
    }
    return s.reduce((a, c) => a+Number(c), 0)
}