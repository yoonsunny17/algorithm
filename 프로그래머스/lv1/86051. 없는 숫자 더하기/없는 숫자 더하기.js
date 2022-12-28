function solution(numbers) {
    
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    const result = arr.filter((i) => !numbers.includes(i)).reduce((a, c) => (a+c), 0)
    
    return result
    
}