function solution(ingredient) {
    let cnt = 0
    let burger = []
    
    ingredient.forEach((el) => {
        burger.push(el)
        if (burger.length >= 4) {
            if (burger.slice(-4).join('') === '1231'){
                burger.pop()
                burger.pop()
                burger.pop()
                burger.pop()
                cnt++
            }
        }
    })
    
    return cnt
}