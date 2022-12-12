function solution(my_string) {
    let str = my_string.split(" ")
    let numb = Number(str[0])
    console.log(numb)
    for (let i=1; i<my_string.length; i++) {
        if (str[i] === "+") {
            numb += Number(str[i+1])
        } else if (str[i] === "-") {
            numb -= Number(str[i+1])
        } else continue
    }
    
    return numb
}