function solution(n, arr1, arr2) {
    let answer = []
    
    let a = arr1.map((el) => el.toString(2).padStart(n, 0))
    let b = arr2.map((el) => el.toString(2).padStart(n, 0))
    
    let sumArr = []
    
    for (let i=0; i<n; i++){
        sumArr.push(String(+a[i] + +b[i]).padStart(n, 0))
    }
    
    for (let i of sumArr){
        answer.push(
            i.split('').map((el) => el === '0' ? el = ' ' : el = '#').join('')
        )
    }
    
    return answer
}