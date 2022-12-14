function solution(polynomial) {
    var answer = '';
    // console.log(polynomial.split(" + "))
    const arr = polynomial.split(" + ")
    let xNum = 0
    let num = 0
    
    arr.forEach((info) => {
        if (info.includes("x")) {
            const xArr = info.split("x")
            
            if (xArr[0] === "") {
                xNum += 1
            } else xNum += Number(xArr[0])
        } else {
            num += Number(info)
        }
    })
    
    if (!xNum && !num) return '0'
    if (!xNum) return num.toString()
    xNum = `${xNum==1?'':xNum}`
    if (!num) return `${xNum}x`
    return `${xNum}x + ${num}`
}