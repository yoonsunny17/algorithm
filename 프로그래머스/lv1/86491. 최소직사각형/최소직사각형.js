function solution(sizes) {
    for (let size of sizes){
        size.sort((a, b) => b - a)
    }
    
    const firstArr = sizes.map((el) => el[0])
    const garo = Math.max.apply(null, firstArr.map((el) => el))
    
    const secondArr = sizes.map((el) => el[1])
    const sero = Math.max.apply(null, secondArr.map((el) => el))
    
    return Number(garo*sero)
}